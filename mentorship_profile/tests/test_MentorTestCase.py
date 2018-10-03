from django.test import TestCase
from django.contrib.auth.models import User

from .test_utilities import UserFactory
from ..models import Mentor


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

        self.assertEqual(new_mentor.areas_of_guidance, "unknown")
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
