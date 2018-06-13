from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Pairing
from mentorship_profile.models import Mentor, Mentee
from mentorship_profile.tests.test_utilities import UserFactory


class PairingTestCase(TestCase):
    """Base test class for the Pairing model and views."""

    def create_mentor(self, user):
        """Create and return a new test mentor."""
        mentor = Mentor()
        mentor.profile = user.profile
        mentor.save()
        return mentor

    def create_mentee(self, user):
        """Create and return a new test mentee."""
        mentee = Mentee()
        mentee.profile = user.profile
        mentee.save()
        return mentee

    def create_pairing(self):
        """Create and return a new Pairing."""
        user1 = UserFactory.create()
        user2 = UserFactory.create()
        mentor = self.create_mentor(user1)
        mentee = self.create_mentee(user2)
        test_pairing = Pairing()
        test_pairing.mentor = mentor
        test_pairing.mentee = mentee
        test_pairing.save()
        return test_pairing

    def common_setup(self):
        """Creates a common test setup that.

        Create and return:
            * test_pairing with mentor and mentee, requested by mentor
            * test_user that is logged in, is mentor
        """
        test_pairing = self.create_pairing()
        test_user = User.objects.first()
        test_pairing.request_message = "Wont you be my friend?"
        test_pairing.requested_by = test_pairing.mentor.profile
        test_pairing.save()
        self.client.force_login(test_user)
        return test_pairing, test_user
