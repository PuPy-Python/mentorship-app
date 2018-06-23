from django.test import TestCase, RequestFactory
from ..views import show_homepage_view, show_CoC_view


class GeneralViewsTestCase(TestCase):
    """Unit tests for Homepage and Code of Conduct."""

    def setUp(self):
        """Set up request factory to test page views."""

        self.factory = RequestFactory()

    def test_loading_homepage(self):
        """Test to ensure homepage loads."""

        request = self.factory.get("/")
        response = show_homepage_view(request)
        self.assertEqual(response.status_code, 200)

    def test_loading_CoC(self):
        """Test to ensure code of conduct page loads."""

        request = self.factory.get("/conduct")
        response = show_CoC_view(request)
        self.assertEqual(response.status_code, 200)
