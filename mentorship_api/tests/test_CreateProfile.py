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
                "areas_of_interest": ["career_growth"],
                "mentee_capacity": 3,
                "currently_accepting_mentees": False,
            },
            "mentee": {
                "area_of_interest": "career_growth",
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
            },
            "mentee": {
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
        self.assertIn("areas_of_interest", data["mentor"])
        self.assertIn("mentee_capacity", data["mentor"])
        self.assertIn("mentee", data)
        self.assertIn("area_of_interest", data["mentee"])
        self.assertIn("goals", data["mentee"])
