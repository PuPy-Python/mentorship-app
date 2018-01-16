
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET


from .tokens import account_activation_token
from .forms import (
    UserSignupForm,
    ProfileSignupForm,
    MenteeForm,
    MentorForm
)


def register_mentor_view(request):
    """Mentor registration view."""
    if request.method == "POST":
        user_form = UserSignupForm(request.POST, prefix="user")
        profile_form = ProfileSignupForm(request.POST, prefix="profile")
        mentor_form = MentorForm(request.POST, prefix=("mentor"))

        if (
            user_form.is_valid() and
            profile_form.is_valid() and
            mentor_form.is_valid()
        ):

            user = user_form.save(commit=False)
            user.is_active = False
            user.profile = profile_form.save(commit=False)
            user.save()
            user.profile.save()

            mentor = mentor_form.save(commit=False)
            mentor.profile = user.profile
            mentor.save()

            _send_registration_email(request, user, "mentor")

            return redirect('activate_notification')

    elif request.method == "GET":
        user_form = UserSignupForm(prefix="user")
        profile_form = ProfileSignupForm(prefix="profile")
        mentor_form = MentorForm(prefix="mentor")

    return render(
        request,
        'mentorship_profile/register.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'account_type_form': mentor_form
        }
    )


def register_mentee_view(request):
    """Mentee registration view."""
    if request.method == "POST":
        user_form = UserSignupForm(request.POST, prefix="user")
        profile_form = ProfileSignupForm(request.POST, prefix="profile")
        mentee_form = MenteeForm(request.POST, prefix=("mentee"))

        if (
                user_form.is_valid() and
                profile_form.is_valid() and
                mentee_form.is_valid()
        ):

            user = user_form.save(commit=False)
            user.is_active = False
            user.profile = profile_form.save(commit=False)
            user.save()
            user.profile.save()

            mentee = mentee_form.save(commit=False)
            mentee.profile = user.profile
            mentee.save()

            _send_registration_email(request, user, "mentee")

            return redirect('activate_notification')

    elif request.method == "GET":
        user_form = UserSignupForm(prefix="user")
        profile_form = ProfileSignupForm(prefix="profile")
        mentee_form = MenteeForm(prefix=("mentee"))

    return render(
        request,
        'mentorship_profile/register.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'account_type_form': mentee_form
        }
    )


def _send_registration_email(request, user, acct_type):
    """Given request, user model, and acct type, send a registration email."""
    current_site = get_current_site(request)
    subject = "Activate your PuPPy Mentorship Account"
    message = render_to_string(
        'mentorship_profile/activation_email.html', {
            "user": user,
            "domain": current_site.domain,
            "account_type": acct_type,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user)
        }
    )
    user.email_user(subject, message)


@require_GET
def activate_account_view(request, uidb64, token):
    """Account activation view."""
    user = _get_user_from_uid(uidb64)
    valid_token = account_activation_token.check_token(user, token)

    if user is not None and valid_token:
        user.profile.email_confirmed = True
        user.profile.save()
        login(request, user)
        return render(
            request,
            'mentorship_profile/activation_complete.html',
            {"user": user}
        )
    else:
        # invalid link
        return render(
            request,
            'mentorship_profile/activation_invalid.html'
        )


def _get_user_from_uid(uidb64):
    """Given the uid from the request, return the user for that id or None."""
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        return user
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return None
