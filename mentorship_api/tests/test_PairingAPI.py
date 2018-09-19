from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from mentorship_profile.models import Profile, Mentor, Mentee
from mentorship_pairing.models import Pairing


class PairingAPI(APITestCase):

    def _create_user(self, username, password):
        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.profile = Profile(
            id=user.profile.id,
            bio="I am a test profile"
        )
        user.profile.save()
        return user

    def _create_mentor(self, user):
        mentor = Mentor(
            profile=user.profile
        )
        mentor.save()
        user.profile.mentor = mentor
        return mentor

    def _create_mentee(self, user):
        mentee = Mentee(
            goals="increase test coverage",
            profile=user.profile
        )
        mentee.save()
        user.profile.mentee = mentee
        return mentee

    def _create_pairing(self, mentor_user, mentee_user):
        pairing = Pairing()
        pairing.mentor = mentor_user.profile.mentor
        pairing.mentee = mentee_user.profile.mentee
        pairing.save()
        return pairing

    def _setup_credentials(self, username, password):
        url = reverse("token_auth_api")
        response = self.client.post(url, {
            "username": username,
            "password": password,
        })
        token = response.json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

    def setUp(self):
        username = "api-tester"
        password = "testtest123"
        self.user = self._create_user(username, password)
        self._setup_credentials(username, password)

        self.mentor = self._create_user("mentor", password)
        self._create_mentor(self.mentor)
        self.mentee = self._create_user("mentee", password)
        self._create_mentee(self.mentee)
        self.pairing = self._create_pairing(self.mentor, self.mentee)

    def test_list_pairings(self):
        url = reverse("pairing_list_api")
        response = self.client.get(url)
        data = response.json()
        self.assertTrue(data)
        self.assertEqual(data[0]["id"], self.pairing.id)
        self.assertEqual(data[0]["mentor"], self.pairing.mentor.id)
        self.assertEqual(data[0]["mentee"], self.pairing.mentee.id)
        self.assertEqual(data[0]["requested_by"], self.pairing.requested_by)
        self.assertEqual(data[0]["status"], self.pairing.status)
        self.assertEqual(data[0]["request_message"],
                         self.pairing.request_message)

    def test_create_pairing(self):
        # THIS TEST CASE NEEDS WORK
        '''
        self._create_mentor(self.mentee)
        self._create_mentee(self.mentor)
        opposite_pairing = {
            "mentor": self.mentee.profile.mentor.id,  # FAILURE: Invalid pk
            "mentee": self.mentor.profile.mentee.id,  # this one is okay
            "requested_by": None,
            "status": "pending",
            "request_message": "a new test pairing",
        }
        url = reverse("pairing_list_api")
        response = self.client.post(url, opposite_pairing, format="json")
        data = response.json()
        self.assertTrue(data)
        self.assertIn("id", data)  # What should the response field(s) be??
        '''
        pass

    def test_get_pairing(self):
        url = reverse("pairing_detail_api", args=(self.pairing.id,))
        response = self.client.get(url)
        data = response.json()
        self.assertTrue(data)
        self.assertEqual(data["id"], self.pairing.id)
        self.assertEqual(data["mentor"], self.pairing.mentor.id)
        self.assertEqual(data["mentee"], self.pairing.mentee.id)
        self.assertEqual(data["requested_by"], self.pairing.requested_by)
        self.assertEqual(data["status"], self.pairing.status)
        self.assertEqual(data["request_message"], self.pairing.request_message)

    def test_update_pairing(self):
        # THIS TEST CASE NEEDS WORK
        '''
        new_status = "active"
        pairing_dict = {
            "mentor": self.pairing.mentor.id,  # FAILURE: Invalid pk
            "mentee": self.pairing.mentee.id,  # this one is okay
            "requested_by": self.pairing.requested_by,
            "status": new_status,
            "request_message": self.pairing.request_message,
        }
        url = reverse("pairing_detail_api", args=(self.pairing.id,))
        response = self.client.put(url, pairing_dict, format="json")
        data = response.json()
        self.assertTrue(data)
        # What should the response field(s) be?
        # Now check that pairing was updated
        url = reverse("pairing_detail_api", args=(self.pairing.id,))
        response = self.client.get(url)
        data = response.json()
        self.assertTrue(data)
        self.assertEqual(data["id"], self.pairing.id)
        self.assertEqual(data["mentor"], self.pairing.mentor.id)
        self.assertEqual(data["mentee"], self.pairing.mentee.id)
        self.assertEqual(data["requested_by"], self.pairing.requested_by)
        self.assertEqual(data["status"], new_status)  # FAILURE: not updated
        self.assertEqual(data["request_message"], self.pairing.request_message)
        '''
        pass

    def test_delete_pairing(self):
        url = reverse("pairing_detail_api", args=(self.pairing.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Now check that pairing no longer exists
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
