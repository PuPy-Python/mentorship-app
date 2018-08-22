"""This module defines custom Form classes for the Mentor and Mentee models."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Mentor, Mentee, Profile


class UserSignupForm(UserCreationForm):
    """SignUp form for the User Model."""

    email = forms.CharField(
        required=True,
        label="Email",
    )

    first_name = forms.CharField(
        required=False,
        label="First Name",
        help_text="Optional"
    )

    last_name = forms.CharField(
        required=False,
        label="Last Name",
        help_text="Optional"
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2"
        )


class UserModelForm(forms.ModelForm):
    """UserModel Form for editing after sign up."""

    username = forms.CharField(
        required=True,
        label="Username"
    )

    email = forms.CharField(
        required=True,
        label="Email",
    )

    first_name = forms.CharField(
        required=False,
        label="First Name",
        help_text="Optional"
    )

    last_name = forms.CharField(
        required=False,
        label="Last Name",
        help_text="Optional"
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )


class ProfileSignupForm(forms.ModelForm):
    """Create a form for signing up a Profile Model."""

    slack_handle = forms.CharField(
        required=False,
        label="Slack Handle",
        help_text="PuPPy Slack Team handle (optional)"
    )

    linked_in_url = forms.URLField(
        required=False,
        label="LinkedIn URL",
        help_text="LinkedIn URL (optional)"
    )

    projects_url = forms.URLField(
        required=False,
        label="Code Repo URL",
        help_text="Coding Projects url (e.g. Github, Gitlab, Bitbucket, " +
        "personal site) (optional)"
    )

    bio = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="Bio",
        help_text="Tell us a bit about yourself and your interests."
    )

    class Meta:
        model = Profile
        fields = (
            "slack_handle",
            "linked_in_url",
            "projects_url",
            "bio",
            "years_industry_experience",
        )


class MentorForm(forms.ModelForm):
    """Create a form for the Mentor model."""

    mentee_capacity = forms.IntegerField(
        max_value=5,
        min_value=1
    )

    class Meta:
        model = Mentor
        fields = (
            "areas_of_interest",
            "mentee_capacity",
            "currently_accepting_mentees",
        )


class MenteeForm(forms.ModelForm):
    """Create a form for the Mentee model."""

    goals = forms.CharField(
        widget=forms.Textarea,
        help_text="Tell us a bit about your goals and what you would like a " +
        "mentor can help you with.  (e.g. career goals, technical skills, etc)"
    )

    class Meta:
        model = Mentee
        fields = ("area_of_interest", "goals")
