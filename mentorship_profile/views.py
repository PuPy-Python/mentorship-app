
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .tokens import account_activation_token
from .forms import (
    ProfileSignupForm,
    MenteeForm,
    MentorForm
)
from .models import (Mentor, Mentee)


def register_mentor_view(request):
    """Mentor registration view."""
    if request.method == "POST":
        user_profile_form = ProfileSignupForm(request.POST, prefix="profile")
        mentor_form = MentorForm(request.POST, prefix=("mentor"))

        if user_profile_form.is_valid() and mentor_form.is_valid():
            user = _register_user_profile(user_profile_form)

            mentor = Mentor(profile=user.profile)
            mentor.area_of_expertise =\
                mentor_form.cleaned_data.get("area_of_expertise")
            mentor.mentee_capacity =\
                mentor_form.cleaned_data.get("mentee_capacity")
            mentor.save()

            _send_registration_email(request, user, "mentor")

            return redirect('activate_notification')

    elif request.method == "GET":
        user_profile_form = ProfileSignupForm(prefix="profile")
        mentor_form = MentorForm(prefix="mentor")

    return render(
        request,
        'mentorship_profile/register.html',
        {
            'user_profile_form': user_profile_form,
            'account_type_form': mentor_form
        }
    )


def register_mentee_view(request):
    """Mentee registration view."""
    if request.method == "POST":
        user_profile_form = ProfileSignupForm(request.POST, prefix="profile")
        mentee_form = MenteeForm(request.POST, prefix=("mentee"))

        if user_profile_form.is_valid() and mentee_form.is_valid():
            user = _register_user_profile(user_profile_form)

            mentee = Mentee(profile=user.profile)
            mentee.area_of_interest =\
                mentee_form.cleaned_data.get("area_of_interest")
            mentee.goals =\
                mentee_form.cleaned_data.get("goals")
            mentee.save()

            _send_registration_email(request, user, "mentee")

            return redirect('activate_notification')

    elif request.method == "GET":
        user_profile_form = ProfileSignupForm(prefix="profile")
        mentee_form = MenteeForm(prefix=("mentee"))

    return render(
        request,
        'mentorship_profile/register.html',
        {
            'user_profile_form': user_profile_form,
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


def _register_user_profile(profile_form):
    """Given a valid profile form, register the profile and return the user."""
    user = profile_form.save(commit=False)
    user.is_active = False
    user.save()
    user.refresh_from_db()  # Send signals to create Profile model.
    user.profile.slack_handle =\
        profile_form.cleaned_data.get("slack_handle")
    user.profile.linked_in_url =\
        profile_form.cleaned_data.get("linked_in_url")
    user.profile.repo_url =\
        profile_form.cleaned_data.get("repo_url")
    user.profile.bio =\
        profile_form.cleaned_data.get("bio")
    user.save()
    return user


def activate_account_view(request, uidb64, token):
    """Account activation view."""
    if request.method == "GET":
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        valid_token = account_activation_token.check_token(user, token)
        if user is not None and valid_token:
            user.profile.email_confirmed = True
            user.save()
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
