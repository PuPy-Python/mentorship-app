"""This module defines custom Form classes for the Mentor and Mentee models."""

# from registration.forms import RegistrationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Mentor, Mentee


class ProfileSignupForm(UserCreationForm):
    """Create a form for signing up a Profile Model."""

    slack_handle = forms.CharField(
        required=False,
        label="Slack Handle",
        help_text="PuPPy Slack Team handle (optional)"
    )

    linked_in_url = forms.URLField(
        required=False,
        label="Linked In URL",
        help_text="Linked in URL (optional)"
    )

    repo_url = forms.URLField(
        required=False,
        label="Code Repo URL",
        help_text="Code repository url (e.g. Github, Gitlab, Bitbucket)" +
        "(optional)"
    )

    bio = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="Bio",
        help_text="Tell us a bit about yourself and your interests."
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "slack_handle",
            "linked_in_url",
            "repo_url",
            "bio",
        )


class MentorForm(forms.ModelForm):
    """Create a form for the Mentor model."""

    mentee_capacity = forms.IntegerField(
        max_value=5,
        min_value=1
    )

    class Meta:
        model = Mentor
        fields = ("area_of_expertise", "mentee_capacity",)


class MenteeForm(forms.ModelForm):
    """Create a form for the Mentee model."""

    goals = forms.CharField(
        widget=forms.Textarea,
    )

    class Meta:
        model = Mentee
        fields = ("area_of_interest", "goals")
