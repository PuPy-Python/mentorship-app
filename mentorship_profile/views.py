
import re

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET, require_http_methods


from .tokens import account_activation_token
from .forms import (
    UserSignupForm,
    UserModelForm,
    ProfileSignupForm,
    MenteeForm,
    MentorForm
)
# from .models import Profile

ACCOUNT_TYPE_FORMS = {
    "mentor": MentorForm,
    "mentee": MenteeForm
}


def show_homepage_view(request):
    """Homepage view.

    Display the homepage template for PuPPy Mentorship."""

    return render(request, "mentorship/homepage.html")


def show_CoC_view(request):
    """Code of conduct view.

    Display the code of conduct page."""

    return render(request, "mentorship/conduct.html")


def register_user_view(request, account_type):
    """User registration view.

    param `account_type` is a string which determines which ('mentor' or
    'mentee') type of user to register.
    """
    if not _is_valid_account_type(account_type):
        raise Http404("Page not found.")

    if request.method == "POST":
        user_model_form = UserSignupForm(request.POST, prefix="user")
        profile_form = ProfileSignupForm(request.POST, prefix="profile")
        account_type_form = ACCOUNT_TYPE_FORMS[account_type](
            request.POST,
            prefix=(account_type)
        )

        if (
            user_model_form.is_valid() and
            profile_form.is_valid() and
            account_type_form.is_valid()
        ):

            user = user_model_form.save(commit=False)
            user.profile = profile_form.save(commit=False)
            user.save()
            user.profile.save()

            account_type_instance = account_type_form.save(commit=False)
            account_type_instance.profile = user.profile
            account_type_instance.save()

            _send_registration_email(request, user, account_type)

            return redirect('activate_notification')

    elif request.method == "GET":
        user_model_form = UserSignupForm(prefix="user")
        profile_form = ProfileSignupForm(prefix="profile")
        account_type_form = ACCOUNT_TYPE_FORMS[account_type](
            prefix=account_type
        )

    return render(
        request,
        'mentorship_profile/register.html',
        {
            'user_form': user_model_form,
            'profile_form': profile_form,
            'account_type_form': account_type_form
        }
    )


def _is_valid_account_type(account_type):
    """Validate the `account_type` param, must be 'mentor' or 'mentee'."""
    return account_type in ACCOUNT_TYPE_FORMS.keys()


def _send_registration_email(request, user, acct_type):
    """Given request, user model, and acct type, send a registration email."""
    current_site = get_current_site(request)
    subject = "Activate your PuPPy Mentorship Account"

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_token = account_activation_token.make_token(user)

    url_token = uid.decode('utf-8') + '/' + activation_token

    message = render_to_string(
        'mentorship_profile/activation_email.html', {
            "user": user,
            "domain": current_site.domain,
            "account_type": acct_type,
            "url_token": url_token
        }
    )
    user.email_user(subject, message)


@require_GET
def activate_account_view(request, url_token):
    """Account activation view."""
    uid, token = _parse_url_token(url_token)

    user = _get_user_from_uid(uid)
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


def _parse_url_token(url_token):
    """Given activation token from url, parse into expected components."""
    match = re.fullmatch(
        '^([0-9A-Za-z_\-]+)/([0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        url_token
    )
    if match:
        return match.group(1), match.group(2)
    return None, None


@login_required()
@require_GET
def profile_private_view(request):
    """Display the user's private profile view.

    GET: Render user's private profile view.
    """

    # TODO: return notifications and pairings

    return render(
        request,
        'mentorship_profile/profile_private.html'
    )


@login_required()
@require_http_methods(["GET", "POST"])
def profile_edit_view(request):
    """View to handle viewing and updating user's profile info.

    GET: Render user, profile, and mentor/mentee forms.

    POST:
        Update user, profile, and mentor/mentee model information.
        Redirect to 'private_profile' view.
    """
    if request.method == 'POST':
        user_model_form = UserModelForm(
            request.POST,
            prefix="user",
            instance=request.user
        )
        profile_model_form = ProfileSignupForm(
            request.POST,
            prefix="profile",
            instance=request.user.profile
        )
        forms = [user_model_form, profile_model_form]

        if request.user.profile.is_mentor():
            mentor_form = MentorForm(
                request.POST,
                prefix="mentor",
                instance=request.user.profile.mentor
            )
            forms.append(mentor_form)

        if request.user.profile.is_mentee():
            mentee_form = MenteeForm(
                request.POST,
                prefix="mentee",
                instance=request.user.profile.mentee
            )
            forms.append(mentee_form)

        forms_is_valid_list = []
        for form in forms:
            forms_is_valid_list.append(form.is_valid())

        if all(forms_is_valid_list):
            for form in forms:
                form.save()
            return redirect("private_profile")

    elif request.method == 'GET':
        forms = [
            UserModelForm(
                instance=request.user,
                prefix="user"
            ),
            ProfileSignupForm(
                instance=request.user.profile,
                prefix="profile"
            )
        ]

        if request.user.profile.is_mentor():
            forms.append(
                MentorForm(
                    instance=request.user.profile.mentor,
                    prefix="mentor"
                )
            )

        if request.user.profile.is_mentee():
            forms.append(
                MenteeForm(
                    instance=request.user.profile.mentee,
                    prefix="mentee"
                )
            )

    return render(
        request,
        'mentorship_profile/profile_edit.html',
        {
            "forms": forms
        }
    )


@login_required
@require_GET
def profile_public_view(request, username):
    """Given a username, display the publically available profile data.

    GET:
        Render public profile for <username>.
        If is_paired_with_current_user(username), display contact info.
    """
    user = User.objects.filter(username=username).first()
    if user:
        return render(
            request,
            "mentorship_profile/profile_public.html",
            {"user_instance": user}
        )

    raise Http404('User %s not found.' % username)


@login_required
@require_GET
def mentor_list_view(request):
    """List View for Mentors."""
    # TODO: this view
    pass


@login_required
@require_GET
def mentee_list_view(request):
    """List view for Mentees."""
    # TODO: this view
    pass
