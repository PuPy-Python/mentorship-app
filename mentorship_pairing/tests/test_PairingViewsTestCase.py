from django.contrib.auth.models import User
from django.test import (
    Client,
    RequestFactory
)
from django.urls import reverse

from .test_utilities import PairingTestCase
from ..models import Pairing
from ..views import ACCEPT_VALUE, REJECT_VALUE
from mentorship_profile.tests.test_utilities import UserFactory
from mentorship_profile.models import Mentor, Mentee


class PairingViewsTestCase(PairingTestCase):
    """Unit and functional tests for Pairing views."""

    def setUp(self):
        """Set up for all PairingViews tests."""
        self.client = Client()
        self.request = RequestFactory()

    def login_test_user(self, user):
        """Given a user, give them proper credentials and log them in."""
        # user.password1 = "supersecret"
        # user.password2 = "supersecret"
        user.save()
        self.client.force_login(user)

    def test_valid_get_simple_pairing_detail_view(self):
        """Test pairing_detail_view with valid get respone."""
        test_pairing = self.create_pairing()
        test_user = UserFactory.create()
        self.client.force_login(test_user)
        url = '/pairing/%s/' % test_pairing.id
        res = self.client.get(url)
        self.assertEquals(
            'mentorship_pairing/pairing_detail.html',
            res.templates[0].name
        )
        self.assertFalse(test_pairing.is_user_in_pairing(test_user))
        self.assertContains(res, test_pairing.mentor.profile.user.username)
        self.assertContains(res, test_pairing.mentee.profile.user.username)
        self.assertNotContains(res, test_user.email)

    def test_404_get_pairing_detail_view(self):
        """Test that pairing_detail_view returns a 404 for bad id."""
        test_pairing = self.create_pairing()
        test_user = User.objects.first()
        self.client.force_login(test_user)
        url = '/pairing/42/'
        res = self.client.get(url)
        self.assertEquals(
            404,
            res.status_code
        )

    def test_get_pairing_detail_view_current_user_and_active(self):
        """Test that the pairing_detail_view displays more info.

        Should display contact info IF:
            * current user is in pairing AND
        """
        test_pairing = self.create_pairing()
        test_user = User.objects.first()
        self.client.force_login(test_user)
        self.assertTrue(test_pairing.is_user_in_pairing(test_user))
        url = '/pairing/%s/' % test_pairing.id
        res = self.client.get(url)
        self.assertEquals(
            'mentorship_pairing/pairing_detail.html',
            res.templates[0].name
        )
        self.assertContains(res, test_pairing.mentor.profile.user.username)
        self.assertContains(res, test_pairing.mentee.profile.user.username)
        self.assertContains(res, test_pairing.mentor.profile.user.email)
        self.assertContains(res, test_pairing.mentee.profile.user.email)

    def test_get_pairing_respond_view(self):
        """Test get request for pairing_respond returns expected form."""
        test_pairing = self.create_pairing()
        test_user = User.objects.first()
        test_pairing.request_message = "Wont you be my friend?"
        test_pairing.requested_by = test_pairing.mentor.profile
        test_pairing.save()
        self.client.force_login(test_user)
        url = '/pairing/%s/respond/' % test_pairing.id
        res = self.client.get(url)

        self.assertContains(res, test_pairing.request_message)
        self.assertContains(
            res,
            "{} has requested to pair with you!".format(
                test_pairing.requestor.user.username
            )
        )

    def test_valid_post_pairing_respond_accept(self):
        """Test that accepting a pairing req with valid form updates model"""
        test_pairing = self.create_pairing()
        test_user = User.objects.first()
        test_pairing.request_message = "Wont you be my friend?"
        test_pairing.requested_by = test_pairing.mentor.profile
        test_pairing.save()
        self.client.force_login(test_user)
        url = '/pairing/%s/respond/' % test_pairing.id
        res = self.client.post(url, {'response': ACCEPT_VALUE}, follow=True)

        self.assertEquals(
            'mentorship_pairing/pairing_accepted.html',
            res.templates[0].name
        )
        # TODO: Test contents

    def test_valid_post_pairing_respond_reject(self):
        """Test that accepting a pairing req with valid form updates model"""
        test_pairing = self.create_pairing()
        test_user = User.objects.first()
        test_pairing.request_message = "Wont you be my friend?"
        test_pairing.requested_by = test_pairing.mentor.profile
        test_pairing.save()
        self.client.force_login(test_user)
        url = '/pairing/%s/respond/' % test_pairing.id
        res = self.client.post(url, {'response': REJECT_VALUE}, follow=True)

        self.assertEquals(
            'mentorship_pairing/pairing_rejected.html',
            res.templates[0].name
        )
        # TODO: Test contents

    def test_invalid_post_pairing_respond_accept_404(self):
        """Test that an invalid POST doesn't update model, raise error."""
        test_pairing, test_user = self.common_setup()
        url = url = '/pairing/%s/respond/' % 10000
        res = self.client.post(url, {'response': ACCEPT_VALUE})
        self.assertEquals(404, res.status_code)

    def test_invalid_post_pairing_respond_accept(self):
        """Test that an invalid POST doesn't update model, raise error."""
        test_pairing, test_user = self.common_setup()
        url = url = '/pairing/%s/respond/' % test_pairing.id
        res = self.client.post(url, {'response': 'foobar'})
        self.assertEquals(400, res.status_code)

    def test_get_pairing_request_view(self):
        """Test GET pairing_request_view returns form for Pairing Request."""
        test_user1 = UserFactory.create()
        self.client.force_login(test_user1)
        test_user2 = UserFactory.create()
        mentor = self.create_mentor(test_user1)
        mentee = self.create_mentee(test_user2)
        url = '/pairing/request/%s/%s/' % (mentor.id, mentee.id)
        res = self.client.get(url)
        self.assertEquals(
            'mentorship_pairing/pairing_request.html',
            res.templates[0].name
        )

    def test_404_get_pairing_request_bad_ids(self):
        """Test that GET with bad ids returns 404."""
        test_user = UserFactory.create()
        self.client.force_login(test_user)
        bad_urls = [
            '/pairing/request///',
            '/pairing/request/foo/bar/',
            '/pairing/request/2001/2010/',

        ]
        for bad_url in bad_urls:
            res = self.client.get(bad_url)
            self.assertEquals(404, res.status_code)

    def test_valid_post_pairing_request(self):
        """Test a valid POST request for pairing_request_view.

        SHOULD:
            * create pairing with form data, status=pending
            * create notification for Requestee
            * send an email
            * redirect to 'Thank you, a notification has been sent.'
        """
        test_user1 = UserFactory.create()
        test_user2 = UserFactory.create()
        self.client.force_login(test_user1)
        mentor = self.create_mentor(test_user1)
        mentee = self.create_mentee(test_user2)
        url = '/pairing/request/%s/%s/' % (mentee.id, mentor.id)
        res = self.client.post(
            url,
            {'pairing-request_message': "Won't you be my friend?"},
            follow=True
        )
        self.assertEquals(
            'mentorship_profile/profile_private.html',
            res.templates[0].name
        )
        new_pairing = Pairing.objects.first()
        self.assertEquals(mentor, new_pairing.mentor)
        self.assertEquals(mentee, new_pairing.mentee)
        self.assertEquals(test_user1.profile, new_pairing.requested_by)
        self.assertEquals(
            new_pairing.request_message,
            "Won't you be my friend?"
        )

    # def test_invalid_post_pairing_request(self):
    #     """Invalid data should not create model, return error."""
    #     self.assertTrue(False)

    def test_get_pairing_discontinue_view(self):
        """Should return expected form."""
        test_pairing, test_user = self.common_setup()
        url = '/pairing/%s/discontinue/' % test_pairing.id
        res = self.client.get(url)
        self.assertEquals(200, res.status_code)
        self.assertEquals(
            'mentorship_pairing/pairing_discontinue.html',
            res.templates[0].name
        )

    def test_valid_post_pairing_discontinue(self):
        """Valid POST should change Pairing status."""
        test_pairing, test_user = self.common_setup()
        url = '/pairing/%s/discontinue/' % test_pairing.id
        res = self.client.post(url, {'discontinue': 'True'}, follow=True)
        test_pairing = Pairing.objects.filter(id=test_pairing.id).first()
        self.assertEquals(
            'discontinued',
            test_pairing.status
        )
        self.assertEquals(
            'mentorship_profile/profile_private.html',
            res.templates[0].name
        )

    def test_invalid_post_pairing_discontinue(self):
        """Invalid POST won't change pairing, should raise error."""
        test_pairing, test_user = self.common_setup()
        url = '/pairing/%s/discontinue/' % test_pairing.id
        res = self.client.post(url, {'discontinue': 'False'}, follow=True)
        self.assertEquals(400, res.status_code)
        res2 = self.client.post(url, {}, follow=True)
        self.assertEquals(400, res2.status_code)
