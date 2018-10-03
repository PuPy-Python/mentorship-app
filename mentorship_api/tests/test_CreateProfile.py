from django.urls import reverse
from rest_framework.test import APITestCase


class CreateProfile(APITestCase):
    def test_create_profile(self):
        url = reverse("user_api")
        new_user = {
            "user": {
                "username": "api-tester-create",
                "email": "test-create@test.test",
                "first_name": "Johnny",
                "last_name": "O'Donnell",
                "password": "i@m@Te3est",
                "confirm_password": "i@m@Te3est",
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
        self.assertIn("user_id", data)
        self.assertIn("profile_id", data)
        self.assertIn("mentor_id", data)
        self.assertIn("mentee_id", data)

    def test_create_profile_errors(self):
        url = reverse("user_api")
        new_user = {
            "user": {
            },
            "profile": {
            },
            "mentor": {
                "dummy": "dummy",
            },
            "mentee": {
                "dummy": "dummy",
            },
        }
        response = self.client.post(url, new_user, format="json")
        data = response.data
        self.assertIn("user", data)
        self.assertIn("username", data["user"])
        self.assertIn("first_name", data["user"])
        self.assertIn("last_name", data["user"])
        self.assertIn("email", data["user"])
        self.assertIn("profile", data)
        self.assertIn("bio", data["profile"])
        self.assertIn("mentor", data)
        self.assertIn("areas_of_guidance", data["mentor"])
        self.assertIn("mentee_capacity", data["mentor"])
        self.assertIn("mentee", data)
        self.assertIn("areas_of_guidance", data["mentee"])
        self.assertIn("goals", data["mentee"])

    def test_create_profile_errors_no_mentor_mentee(self):
        url = reverse("user_api")
        new_user = {
            "user": {
            },
            "profile": {
            },
        }
        response = self.client.post(url, new_user, format="json")
        data = response.data
        self.assertIn("user", data)
        self.assertIn("username", data["user"])
        self.assertIn("first_name", data["user"])
        self.assertIn("last_name", data["user"])
        self.assertIn("email", data["user"])
        self.assertIn("profile", data)
        self.assertIn("bio", data["profile"])

    def test_create_profile_errors_no_password(self):
        url = reverse("user_api")
        new_user = {
            "user": {
                "username": "api-tester-create",
                "email": "test-create@test.test",
                "first_name": "Johnny",
                "last_name": "O'Donnell",
            },
            "profile": {
            },
        }
        response = self.client.post(url, new_user, format="json")
        self.assertEqual(response.status_code, 400)
        data = response.data
        self.assertIn("user", data)
        self.assertIn("non_field_errors", data["user"])

    def test_create_profile_errors_no_password_confirm(self):
        url = reverse("user_api")
        new_user = {
            "user": {
                "username": "api-tester-create",
                "email": "test-create@test.test",
                "first_name": "Johnny",
                "last_name": "O'Donnell",
                "password": "i@m@Te3est",
            },
            "profile": {
            },
        }
        response = self.client.post(url, new_user, format="json")
        self.assertEqual(response.status_code, 400)
        data = response.data
        self.assertIn("user", data)
        self.assertIn("non_field_errors", data["user"])

    def test_create_profile_errors_password_confirm_no_match(self):
        url = reverse("user_api")
        new_user = {
            "user": {
                "username": "api-tester-create",
                "email": "test-create@test.test",
                "first_name": "Johnny",
                "last_name": "O'Donnell",
                "password": "i@m@Te3est",
                "confirm_password": "not_a_match",
            },
            "profile": {
            },
        }
        response = self.client.post(url, new_user, format="json")
        self.assertEqual(response.status_code, 400)
        data = response.data
        self.assertIn("user", data)
        self.assertIn("non_field_errors", data["user"])
