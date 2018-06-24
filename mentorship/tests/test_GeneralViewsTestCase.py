from django.test import TestCase, Client

from mentorship_profile.tests.test_utilities import UserFactory


class GeneralViewsTestCase(TestCase):
    """Unit tests for Homepage and Code of Conduct."""

    def setUp(self):
        """Set up request factory to test page views."""

        self.client = Client()

    def login_test_user(self, user):
        """Given a user, give them proper credentials and log them in."""

        user.save()
        self.client.force_login(user)

    def test_loading_homepage_logged_out(self):
        """Test to ensure homepage loads.

        Make sure navbar shows correct content for unauthenticated user."""

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mentorship/homepage.html")
        self.assertContains(response, "Login")

    def test_loading_homepage_logged_in(self):
        """Test to ensure homepage loads.

        Make sure navbar shows correct content for authenticated user."""

        test_user = UserFactory.create()
        self.login_test_user(test_user)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mentorship/homepage.html")
        self.assertNotContains(response, "Login")

    def test_loading_CoC(self):
        """Test to ensure code of conduct page loads."""

        response = self.client.get("/conduct/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mentorship/conduct.html")
