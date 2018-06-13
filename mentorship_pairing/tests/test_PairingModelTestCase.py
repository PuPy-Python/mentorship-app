from django.core.exceptions import ValidationError

from .test_utilities import PairingTestCase
from ..models import Pairing
from mentorship_profile.tests.test_utilities import UserFactory
from mentorship_profile.models import Mentor, Mentee


class PairingModelTestCase(PairingTestCase):
    """The Pairing model test case."""

    def test_cant_create_pairing_same_mentor_mentee(self):
        """Test that we can't pair a user with themself."""
        user = UserFactory.create()
        mentor = self.create_mentor(user)
        mentee = self.create_mentee(user)
        new_pairing = Pairing()
        new_pairing.mentor = mentor
        new_pairing.mentee = mentee
        with self.assertRaises(ValidationError):
            new_pairing.save()

    def test_pairing_model_all_fields(self):
        """Test all fields of the pairing model."""
        user1 = UserFactory.create()
        user2 = UserFactory.create()
        mentor = self.create_mentor(user1)
        mentee = self.create_mentee(user2)
        test_pairing = Pairing()
        test_pairing.mentor = mentor
        test_pairing.mentee = mentee
        req_msg = "Please be my friend."
        test_pairing.request_message = req_msg
        test_pairing.save()

        saved_pairing = Pairing.objects.first()
        test_cases = [
            (user1.username, saved_pairing.mentor.profile.user.username),
            (user2.username, saved_pairing.mentee.profile.user.username),
            (req_msg, saved_pairing.request_message),
            ('pending', saved_pairing.status)
        ]
        for case in test_cases:
            self.assertEquals(case[0], case[1])

    def test_active_pairings_manager(self):
        """Test the ActivePairingsManager returns correct subset."""
        test_pairing1 = self.create_pairing()
        test_pairing1.status = 'active'
        test_pairing1.save()

        # Create another pairing, default status of 'pending'.
        self.create_pairing()

        active_pairings = Pairing.active_pairings.all()
        self.assertEquals(len(active_pairings), 1)
        self.assertEquals(test_pairing1, active_pairings[0])

    def test_pending_pairings_manager(self):
        """Test PendingPairingsManager returns correct subset."""
        test_pairing1 = self.create_pairing()
        test_pairing1.status = 'active'
        test_pairing1.save()

        # Create two more pairings, default status of 'pending'.
        pending_pairing1 = self.create_pairing()
        pending_pairing2 = self.create_pairing()

        active_pairings = Pairing.pending_pairings.all()
        self.assertEquals(len(active_pairings), 2)
        self.assertEquals(pending_pairing1, active_pairings[0])
        self.assertEquals(pending_pairing2, active_pairings[1])

    def test_requestor_requestee_properties(self):
        """Test the requestor and requestee properties."""

        test_pairing = self.create_pairing()

        # These are not assigned by default - requestor and requestee should
        # be none.
        self.assertIsNone(test_pairing.requested_by)
        self.assertIsNone(test_pairing.requestor)
        self.assertIsNone(test_pairing.requestee)

        test_pairing.requested_by = test_pairing.mentor.profile
        test_pairing.save()

        self.assertTrue(
            test_pairing.requested_by is test_pairing.mentor.profile)
        self.assertTrue(test_pairing.requestor is test_pairing.mentor.profile)
        self.assertTrue(test_pairing.requestee is test_pairing.mentee.profile)
        self.assertTrue(test_pairing.requestor is test_pairing.requested_by)

        test_pairing_2 = self.create_pairing()
        self.assertIsNone(test_pairing_2.requested_by)
        self.assertIsNone(test_pairing_2.requestor)
        self.assertIsNone(test_pairing_2.requestee)

        # For completeness, we test the other way - mentee is the requestor.
        test_pairing_2.requested_by = test_pairing_2.mentee.profile
        test_pairing_2.save()

        self.assertTrue(
            test_pairing_2.requested_by is test_pairing_2.mentee.profile)
        self.assertTrue(
            test_pairing_2.requestor is test_pairing_2.mentee.profile)
        self.assertTrue(
            test_pairing_2.requestee is test_pairing_2.mentor.profile)
        self.assertTrue(
            test_pairing_2.requestor is test_pairing_2.requested_by)
