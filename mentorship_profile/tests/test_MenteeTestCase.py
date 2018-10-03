from django.contrib.auth.models import User
from django.test import TestCase

from .test_utilities import UserFactory
from ..models import Mentee, Mentor, AREAS_OF_GUIDANCE


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

        self.assertEqual(new_mentee.areas_of_guidance, "unknown")
        self.assertEqual(new_mentee.profile, User.objects.first().profile)

    def test_mentee_areas_exceed_max_length(self):
        actual = len(",".join(
            map(lambda x: x[0], AREAS_OF_GUIDANCE)
        ))
        max_allowed = next(
            x for x in Mentee._meta.fields if x.attname == "areas_of_guidance"
        ).max_length
        self.assertLessEqual(actual, max_allowed)
