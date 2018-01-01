from unittest.mock import MagicMock
import factory
import re
from django.contrib.auth.models import User
from django.test import (
    Client,
    TestCase,
    RequestFactory,
)
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from .forms import ProfileSignupForm, MentorForm, MenteeForm
from .models import Profile, Mentor, Mentee
from .tokens import AccountActivationTokenGenerator, account_activation_token
from .views import (
    _send_registration_email,
    _register_user_profile
)


class UserFactory(factory.django.DjangoModelFactory):
    """Define a factory for creating user objects."""

    class Meta:
        """Assign a model."""

        model = User

    username = factory.Sequence(lambda n: "Test user {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@foo.com".format(x.username.replace(" ", ""))
    )


class ProfileTestCase(TestCase):
    """The profile model test case."""

    def test_create_user_creates_profile(self):
        """Test that creating a user creates a profile."""
        user = UserFactory.create()
        self.assertEqual(user, Profile.objects.all().first().user)

    def test_all_profile_fields(self):
        """Test saving a profile exercising fields."""
        fake_bio = "Live long and prosper."
        fake_linked_in_url = "www.linkedin.com/in/all_the_spam"
        fake_repo_url = "www.github.com/bob"

        profile = UserFactory.create().profile
        profile.bio = fake_bio
        profile.linked_in_url = fake_linked_in_url
        profile.repo_url = fake_repo_url
        profile.save()

        test_profile = Profile.objects.first()
        self.assertEqual(test_profile.bio, fake_bio)
        self.assertEqual(test_profile.linked_in_url, fake_linked_in_url)
        self.assertEqual(test_profile.repo_url, fake_repo_url)


class MentorTestCase(TestCase):
    """Unit tests for the Mentor model."""

    def create_mentor(self):
        """Helper function to creat Mentor instances."""
        new_user = UserFactory.create()
        new_mentor = Mentor(profile=new_user.profile)
        new_mentor.save()
        return new_mentor

    def test_default_mentor_creation(self):
        """Test default values for newly created mentor."""
        new_mentor = self.create_mentor()

        self.assertEqual(new_mentor.area_of_expertise, "unknown")
        self.assertEqual(
            new_mentor.mentee_capacity,
            Mentor.DEFAULT_MENTEE_CAPACITY
        )
        self.assertFalse(new_mentor.currently_accepting_mentees)
        self.assertEqual(new_mentor.profile, User.objects.first().profile)

    def test_approved_mentor_manager(self):
        """Test that ApprovedMentorManager returns only approved mentors."""
        for _ in range(10):
            mentor = self.create_mentor()
            mentor.mentor_status = 'approved'
            mentor.save()

        for _ in range(10):
            mentor = self.create_mentor()
            # create 10 profiles with default mentor_status
            mentor.save()

        self.assertEqual(len(Mentor.objects.all()), 20)
        self.assertEqual(len(Mentor.approved_mentors.all()), 10)

    def test_pending_mentor_manager(self):
        """Test that PendingMentorManager returns only pending mentors."""
        for _ in range(10):
            mentor = self.create_mentor()
            mentor.mentor_status = 'pending'
            mentor.save()

        for _ in range(10):
            mentor = self.create_mentor()
            # create 10 profiles with default mentor_status
            mentor.save()

        self.assertEqual(len(Mentor.objects.all()), 20)
        self.assertEqual(len(Mentor.pending_mentors.all()), 10)


class MenteeTestCase(TestCase):
    """Unit tests for the Mentee model."""

    def create_mentee(self):
        """Helper function to create Mentees."""
        new_user = UserFactory.create()
        new_mentee = Mentee(profile=new_user.profile)
        new_mentee.save()
        return new_mentee

    def test_default_mentee_creation(self):
        """Test default values for newly created mentee."""
        new_mentee = self.create_mentee()

        self.assertEqual(new_mentee.area_of_interest, "unknown")
        self.assertEqual(new_mentee.profile, User.objects.first().profile)


class ProfileFormsTestCase(TestCase):
    """Unit tests for Profile, Mentor, and Mentee Signup forms."""

    def test_valid_profile_form(self):
        """Test all fields of a valid profile form."""
        valid_profile_data = {
            "username": "Fred",
            "email": "Fred@yahoo.com",
            "password1": "supersecret",
            "password2": "supersecret",
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
            "username": "Fred",
            "email": "Fred@yahoo.com",
            "password1": "supersecret",
            "password2": "supersecret2",
            "slack_handle": "freddie",
            "linked_in_url": "weeee",
            "repo_url": "www.github.com",
        }

        test_form = ProfileSignupForm(invalid_profile_data)
        self.assertFalse(test_form.is_valid())

        # We've created errors in the following fields, check for them:
        # - password2
        # - linked_in_url,
        # - bio
        error_fields = ["password2", "linked_in_url", "bio"]
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


class ProfileViewTestCase(TestCase):
    """Unit Tests for profile views and related functions."""

    def setUp(self):
        """Create request and client obects for view tests."""
        self.client = Client()
        self.request = RequestFactory()

    def test_account_activation_token_generator(self):
        """
        Test the AccountActivateTokenGenerator class.

        Token generator should return a hashed value that matches this
        regex pattern, taken from urls.py:
        [0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}
        """
        user = UserFactory.create()
        acct_token_generator = AccountActivationTokenGenerator()
        test_token = acct_token_generator.make_token(user)

        regex_match = re.search(
            '[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}',
            test_token
        )

        self.assertEqual(test_token, regex_match.string)
        self.assertTrue(acct_token_generator.check_token(user, test_token))

    def test_register_user_profile_returns_valid_user(self):
        """
        Test _register_user_profile helper function.

        Note: form has been validated prior to calling _register_user_profile.
        """
        req_form_params = {
            "username": "bob",
            "email": "bob@gmail.com",
            "password1": "supersecret",
            "password2": "supersecret",
            "bio": "Some bio stuff."
        }

        # Create a valid Profile Signup form and call _register_user_profile
        test_form = ProfileSignupForm(req_form_params)
        self.assertTrue(test_form.is_valid())
        test_user = _register_user_profile(test_form)

        # Grab what should be the same user from the database.
        saved_user = User.objects.first()

        self.assertEqual(test_user.username, saved_user.username)
        self.assertEqual(test_user.profile, saved_user.profile)

    def test_valid_activate_account_view(self):
        """Test the activate_account_view with a valid user and token."""
        user = UserFactory.create()
        self.assertFalse(user.profile.email_confirmed)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)

        res = self.client.get(reverse(
            'activate_account',
            kwargs={
                "uidb64": uid,
                "token": token
            }
        ))

        # Valid response should have 200 status code and the html should
        # contain the username.
        self.assertEqual(res.status_code, 200)
        self.assertTrue(user.username in res.content.decode('utf-8'))

        # TODO: Check that user.profile.email_confirmed is now True.  HOW?!

    def test_invalid_activate_account_view_no_token(self):
        """Test the activate_account_view won't work w/ bad token input."""
        uid = "bob"
        token = "supersecrettoken"
        url = "/activate_account/" + uid + "/" + token

        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)

    def test_invalid_activate_account_view_with_user_bad_token(self):
        """Test activate_account_view with wrong user token."""
        user = UserFactory.create()
        user2 = UserFactory.create()
        self.assertFalse(user.profile.email_confirmed)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user2)

        res = self.client.get(reverse(
            'activate_account',
            kwargs={
                "uidb64": uid,
                "token": token
            }
        ))
        self.assertTrue(b"Invalid activation link" in res.content)
        self.assertEqual(
            'mentorship_profile/activation_invalid.html',
            res.templates[0].name
        )

    def test_send_registration_email(self):
        """Test that we can send a formatted email."""
        user = UserFactory.create()
        test_domain = "127.0.0.1"
        test_uid = urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8')
        test_token = account_activation_token.make_token(user)

        # mock the email_user method so we can test how we build the email.
        user.email_user = MagicMock()

        self.request.user = user
        self.request.get_host = lambda: test_domain
        _send_registration_email(self.request, user, "mentor")
        subject, message = user.email_user.call_args[0]

        # message is dynamically generated by template, verify that certain
        # values are present.
        self.assertTrue(test_domain in message)
        self.assertTrue(test_uid in message)
        self.assertTrue(user.username in message)
        self.assertTrue(test_token in message)
        self.assertEqual(subject, "Activate your PuPPy Mentorship Account")

    def test_get_register_mentor_view(self):
        """Test get method with register_mentor_view."""
        res = self.client.get("/signup/mentor", follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            'mentorship_profile/register.html',
            res.templates[0].name
        )

    def test_post_register_mentor_view(self):
        """Test post valid user data with register_mentor_view."""
        mentor_data = {
            "profile-username": "bob",
            "profile-email": "bob@gmail.com",
            "profile-password1": "supersecret",
            "profile-password2": "supersecret",
            "profile-bio": "Very personal information.",
            "mentor-area_of_expertise": "backend devops",
            "mentor-mentee_capacity": "2",
        }
        res = self.client.post(
            "/signup/mentor/",
            mentor_data,
            follow=True
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            'mentorship_profile/activate_notification.html',
            res.templates[0].name
        )
        user = User.objects.first()
        self.assertEqual(
            user.username,
            mentor_data["profile-username"]
        )
        mentor = Mentor.objects.first()
        self.assertEqual(
            user.profile,
            mentor.profile
        )

    def test_post_invalid_data_register_mentor_view(self):
        """Test post invalid user data with register_mentor_view."""
        invalid_mentor_data = {
            "profile-username": "bob",
            "profile-email": "bob@gmail.com",
            "profile-password1": "supersecret",
            "profile-password2": "supersecretLOL",
            "profile-bio": "Very personal information.",
            "mentor-area_of_expertise": "backend devops",
            "mentor-mentee_capacity": "2",
        }
        res = self.client.post(
            "/signup/mentor/",
            invalid_mentor_data,
            follow=True
        )

        # Should be redirected to the same form page.
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            'mentorship_profile/register.html',
            res.templates[0].name
        )

        # User should not have been registered, users should be empty.
        users = User.objects.all()
        self.assertEqual(len(users), 0)

    def test_get_register_mentee_view(self):
        """Test get method with register_mentee_view."""
        res = self.client.get("/signup/mentee/", follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            'mentorship_profile/register.html',
            res.templates[0].name
        )

    def test_post_register_mentee_view(self):
        """Test post valid user data with register_mentee_view."""
        mentee_data = {
            "profile-username": "Joe",
            "profile-email": "bob@gmail.com",
            "profile-password1": "supersecret",
            "profile-password2": "supersecret",
            "profile-bio": "Very personal information.",
            "mentee-area_of_interest": "backend devops",
            "mentee-goals": "Accomplish all the things!",
        }
        res = self.client.post(
            "/signup/mentee/",
            mentee_data,
            follow=True
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            'mentorship_profile/activate_notification.html',
            res.templates[0].name
        )
        user = User.objects.first()
        self.assertEqual(
            user.username,
            mentee_data["profile-username"]
        )
        mentee = Mentee.objects.first()
        self.assertEqual(
            user.profile,
            mentee.profile
        )

    def test_post_invalid_data_register_mentee_view(self):
        """Test post invalid user data with register_mentee_view."""
        invalid_mentee_data = {
            "profile-username": "Joe",
            "profile-email": "bob@gmail.com",
            "profile-password1": "supersecret",
            "profile-password2": "supersecretLOL",
            "profile-bio": "Very personal information.",
            "mentee-area_of_interest": "backend devops",
            "mentee-goals": "Accomplish all the things!",
        }
        res = self.client.post(
            "/signup/mentee/",
            invalid_mentee_data,
            follow=True
        )

        # Should be redirected to the same form page.
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            'mentorship_profile/register.html',
            res.templates[0].name
        )

        # User should not have been registered, users should be empty.
        users = User.objects.all()
        self.assertEqual(len(users), 0)
