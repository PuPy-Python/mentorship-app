from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from mentorship_profile.models import Profile, Mentor, Mentee


class UpdateProfile(APITestCase):
    def setUp(self):
        url = reverse("user_api")

        username = "api-tester-create"
        password = "i@m@Te3est"

        new_user = {
            "user": {
                "username": username,
                "email": "test-create@test.test",
                "first_name": "Johnny",
                "last_name": "O'Donnell",
                "password": password,
                "confirm_password": password,
            },
            "profile": {
                "slack_handle": "johnnyodonnell",
                "linked_in_url": "https://linkedin.com/reidhoffman",
                "projects_url": "https://github.com/johnnyodonnell",
                "bio": "I am a test profile",
                "years_industry_experience": "1-3",
                "email_confirmed": True,
            },
            "mentor": {
                "mentor_status": "approved",
                "areas_of_guidance": ["career_growth"],
                "mentee_capacity": 3,
                "currently_accepting_mentees": False,
            },
            "mentee": {
                "areas_of_guidance": ["career_growth"],
                "goals": "increase our test converage",
            },
        }
        response = self.client.post(url, new_user, format="json")
        data = response.data
        self.user_id = data["user_id"]

        url = reverse("token_auth_api")
        response = self.client.post(url, {
            "username": username,
            "password": password,
        })
        json = response.json()
        token = json["token"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

    def test_update_profile(self):
        url = reverse("user_api")

        updated_user_name = "John"
        updated_profile_bio = "Updating my test profile..."
        updated_mentor_currently_accepting_mentees = True
        updated_mentee_areas_of_guidance = ["job_search_interviews"]

        user_updates = {
            "user": {
                "first_name": updated_user_name,
            },
            "profile": {
                "bio": updated_profile_bio,
            },
            "mentor": {
                "currently_accepting_mentees":
                updated_mentor_currently_accepting_mentees,
            },
            "mentee": {
                "areas_of_guidance": updated_mentee_areas_of_guidance,
            },
        }
        response = self.client.put(url, user_updates, format="json")
        self.assertEqual(response.status_code, 200)

        user = User.objects.get(pk=self.user_id)
        profile = Profile.objects.get(pk=user.profile.id)
        mentor = Mentor.objects.get(pk=user.profile.mentor.id)
        mentee = Mentee.objects.get(pk=user.profile.mentee.id)

        self.assertEqual(user.first_name, updated_user_name)
        self.assertEqual(profile.bio, updated_profile_bio)
        self.assertEqual(mentor.currently_accepting_mentees,
                         updated_mentor_currently_accepting_mentees)
        self.assertEqual(mentee.areas_of_guidance,
                         updated_mentee_areas_of_guidance)


class UpdateProfileNoUpdate(APITestCase):
    def setUp(self):
        url = reverse("user_api")

        username = "api-tester-create"
        password = "i@m@Te3est"

        new_user = {
            "user": {
                "username": username,
                "email": "test-create@test.test",
                "first_name": "Johnny",
                "last_name": "O'Donnell",
                "password": password,
                "confirm_password": password,
            },
            "profile": {
                "slack_handle": "johnnyodonnell",
                "linked_in_url": "https://linkedin.com/reidhoffman",
                "projects_url": "https://github.com/johnnyodonnell",
                "bio": "I am a test profile",
                "years_industry_experience": "1-3",
                "email_confirmed": True,
            },
        }
        response = self.client.post(url, new_user, format="json")
        data = response.data
        self.user_id = data["user_id"]

        url = reverse("token_auth_api")
        response = self.client.post(url, {
            "username": username,
            "password": password,
        })
        json = response.json()
        token = json["token"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

    def test_update_profile(self):
        url = reverse("user_api")

        user_updates = {}

        response = self.client.put(url, user_updates, format="json")
        self.assertEqual(response.status_code, 200)
