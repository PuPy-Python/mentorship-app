from django.test import TestCase

from ..forms import (
    UserSignupForm,
    ProfileSignupForm,
    MentorForm,
    MenteeForm
)


class FormsTestCase(TestCase):
    """Unit tests for Profile, Mentor, and Mentee Signup forms."""

    def test_valid_user_signup_form(self):
        """Test all fields of a valid user signup form."""
        valid_user_data = {
            "username": "Fred",
            "email": "Fred@woohoo.com",
            "first_name": "Marion",
            "last_name": "Berry",
            "password1": "supersecret",
            "password2": "supersecret",
        }

        test_form = UserSignupForm(valid_user_data)
        self.assertTrue(test_form.is_valid())

    def test_invalid_user_signup_form(self):
        """Test all fields of an invalid user signup form."""
        invalid_user_data = {
            "username": None,
            "email": "yippeee",
            "password1": "supersecret",
            "password2": "supersecret2",
        }

        test_form = UserSignupForm(invalid_user_data)
        self.assertFalse(test_form.is_valid())

        # We've created errors in the following fields, check for them:
        # - username,
        # - email
        # - password2
        error_fields = ["username", "email", "password2"]
        for error in error_fields:
            self.assertTrue(error in test_form.errors)

    def test_valid_profile_form(self):
        """Test all fields of a valid profile form."""
        valid_profile_data = {
            "slack_handle": "freddie",
            "linked_in_url": "www.linkedin.com",
            "repo_url": "www.github.com",
            "bio": "Very personal info very required."
        }

        test_form = ProfileSignupForm(valid_profile_data)
        self.assertTrue(test_form.is_valid())

    def test_invalid_profile_form(self):
        """Test some form validation."""
        invalid_profile_data = {
            "slack_handle": "freddie",
            "linked_in_url": "weeee",
            "repo_url": "www.github.com",
        }

        test_form = ProfileSignupForm(invalid_profile_data)
        self.assertFalse(test_form.is_valid())

        # We've created errors in the following fields, check for them:
        # - linked_in_url,
        # - bio
        error_fields = ["linked_in_url", "bio"]
        for error in error_fields:
            self.assertTrue(error in test_form.errors)

    def test_valid_mentor_form(self):
        """Test all fields of a valid mentor form."""
        valid_mentor_data = {
            "mentee_capacity": 2,
            "area_of_expertise": "backend devops"
        }

        test_form = MentorForm(valid_mentor_data)
        self.assertTrue(test_form.is_valid())

    def test_invalid_mentor_form(self):
        """Test some form validation."""
        invalid_mentor_data = {
            "mentee_capacity": 8,
            "area_of_expertise": "life, the universe, and everything"
        }

        test_form = MentorForm(invalid_mentor_data)
        self.assertFalse(test_form.is_valid())

        # We've created errors in the following fields, check for them:
        # - mentee_capacity
        # - area_of_expertise
        error_fields = ["mentee_capacity", "area_of_expertise"]
        for error in error_fields:
            self.assertTrue(error in test_form.errors)

    def test_valid_mentee_form(self):
        """Test all fields of a valid mentor form."""
        valid_mentee_data = {
            "goals": "Some meaningful goals.",
            "area_of_interest": "backend devops"
        }

        test_form = MenteeForm(valid_mentee_data)
        self.assertTrue(test_form.is_valid())

    def test_invalid_mentee_form(self):
        """Test some form validation."""
        invalid_mentee_data = {
            "area_of_interest": "life, the universe, and everything"
        }

        test_form = MenteeForm(invalid_mentee_data)
        self.assertFalse(test_form.is_valid())

        # We've created errors in the following fields, check for them:
        # - goals
        # - area_of_interest
        error_fields = ["goals", "area_of_interest"]
        for error in error_fields:
            self.assertTrue(error in test_form.errors)
