from django.contrib.auth.models import User
from django.test import TestCase

from .test_utilities import UserFactory
from ..models import Mentee


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
