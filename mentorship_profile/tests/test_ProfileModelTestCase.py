from django.test import TestCase

from .test_utilities import UserFactory
from ..models import Profile


class ProfileModelTestCase(TestCase):
    """The profile model test case."""

    def test_create_user_creates_profile(self):
        """Test that creating a user creates a profile."""
        user = UserFactory.create()
        self.assertEqual(user, Profile.objects.all().first().user)

    def test_all_profile_fields(self):
        """Test saving a profile exercising fields."""
        fake_bio = "Live long and prosper."
        fake_linked_in_url = "www.linkedin.com/in/all_the_spam"
        fake_repo_url = "www.example.com/bob"
        fake_years_industry_experience = "0-1"

        profile = UserFactory.create().profile
        profile.bio = fake_bio
        profile.linked_in_url = fake_linked_in_url
        profile.projects_url = fake_repo_url
        profile.years_industry_experience = fake_years_industry_experience
        profile.save()

        test_profile = Profile.objects.first()
        self.assertEqual(test_profile.bio, fake_bio)
        self.assertEqual(test_profile.linked_in_url, fake_linked_in_url)
        self.assertEqual(test_profile.projects_url, fake_repo_url)
        self.assertEqual(test_profile.years_industry_experience,
                         fake_years_industry_experience)

    # TODO: Test is_mentor convenience method
    # def test_is_approved_mentor(self):
    #     """Test the is_mentor convenience method on the profile model."""
