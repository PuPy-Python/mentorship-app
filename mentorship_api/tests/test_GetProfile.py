from unittest import skipIf
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from mentorship_profile.models import Profile, Mentor, Mentee


class GetProfile(APITestCase):
    def setUp(self):
        password = "testtest123"
        self.user = User.objects.create_user(username="api-tester",
                                             password=password,
                                             first_name="Johnny",
                                             last_name="O'Donnell",
                                             email="test@test.test")

        self.user.profile = Profile(id=self.user.profile.id,
                                    slack_handle="johnnyodonnell",
                                    linked_in_url="reidhoffman",
                                    projects_url="github.com/johnnyodonnell",
                                    bio="I am a test profile",
                                    years_industry_experience="1-2")
        self.user.profile.save()

        url = reverse("token_auth_api")
        response = self.client.post(url, {
            "username": self.user.username,
            "password": password,
        })
        token = response.json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

    def test_get_profile(self):
        url = reverse("user_api")
        response = self.client.get(url)
        data = response.json()
        self.assertTrue(data)
        self.assertEqual(data["user"]["username"], self.user.username)
        self.assertEqual(data["user"]["first_name"], self.user.first_name)
        self.assertEqual(data["user"]["last_name"], self.user.last_name)
        self.assertEqual(data["user"]["email"], self.user.email)

        self.assertTrue(data["profile"])
        self.assertEqual(data["profile"]["id"], self.user.profile.id)
        self.assertEqual(data["profile"]["slack_handle"],
                         self.user.profile.slack_handle)
        self.assertEqual(data["profile"]["linked_in_url"],
                         self.user.profile.linked_in_url)
        self.assertEqual(data["profile"]["projects_url"],
                         self.user.profile.projects_url)
        self.assertEqual(data["profile"]["bio"], self.user.profile.bio)
        self.assertEqual(data["profile"]["years_industry_experience"],
                         self.user.profile.years_industry_experience)

    def test_get_mentor_and_mentee_no_id(self):
        self.user.profile.mentor = Mentor(
                mentor_status="approved",
                areas_of_guidance=["career_growth"],
                mentee_capacity=3,
                currently_accepting_mentees=True,
                profile=self.user.profile)
        self.user.profile.mentor.save()

        self.user.profile.mentee = Mentee(
                areas_of_guidance=["career_growth"],
                goals="increase test coverage",
                profile=self.user.profile)
        self.user.profile.mentee.save()

        url = reverse("user_api")
        self.test_get_mentor_and_mentee(url)

    def test_get_mentor_and_mentee_with_id(self):
        self.user.profile.mentor = Mentor(
                mentor_status="approved",
                areas_of_guidance=["career_growth"],
                mentee_capacity=3,
                currently_accepting_mentees=True,
                profile=self.user.profile)
        self.user.profile.mentor.save()

        self.user.profile.mentee = Mentee(
                areas_of_guidance=["career_growth"],
                goals="increase test coverage",
                profile=self.user.profile)
        self.user.profile.mentee.save()

        url = reverse("user_api_detail", args=[self.user.username])
        self.test_get_mentor_and_mentee(url)

    def test_get_mentor_and_mentee(self, url=None):
        if not url:
            return

        response = self.client.get(url)
        data = response.json()
        self.assertTrue(data)
        self.assertEqual(data["user"]["username"], self.user.username)
        self.assertEqual(data["user"]["first_name"], self.user.first_name)
        self.assertEqual(data["user"]["last_name"], self.user.last_name)
        self.assertEqual(data["user"]["email"], self.user.email)

        self.assertTrue(data["profile"])
        self.assertEqual(data["profile"]["id"], self.user.profile.id)
        self.assertEqual(data["profile"]["slack_handle"],
                         self.user.profile.slack_handle)
        self.assertEqual(data["profile"]["linked_in_url"],
                         self.user.profile.linked_in_url)
        self.assertEqual(data["profile"]["projects_url"],
                         self.user.profile.projects_url)
        self.assertEqual(data["profile"]["bio"], self.user.profile.bio)
        self.assertEqual(data["profile"]["years_industry_experience"],
                         self.user.profile.years_industry_experience)

        self.assertTrue(data["mentor"])
        self.assertEqual(data["mentor"]["mentor_status"],
                         self.user.profile.mentor.mentor_status)
        self.assertEqual(data["mentor"]["areas_of_guidance"],
                         self.user.profile.mentor.areas_of_guidance)
        self.assertEqual(data["mentor"]["mentee_capacity"],
                         self.user.profile.mentor.mentee_capacity)
        self.assertEqual(
                data["mentor"]["currently_accepting_mentees"],
                self.user.profile.mentor.currently_accepting_mentees)

        self.assertTrue(data["mentee"])
        self.assertEqual(data["mentee"]["areas_of_guidance"],
                         self.user.profile.mentee.areas_of_guidance)
        self.assertEqual(data["mentee"]["goals"],
                         self.user.profile.mentee.goals)
