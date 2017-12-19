import factory
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile, Mentor, Mentee


class UserFactory(factory.django.DjangoModelFactory):
    """Define a factory for creating user objects."""

    class Meta:
        """Assign a model."""

        model = User

    username = factory.Sequence(lambda n: "Test user {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@foo.com".format(x.username.replace(" ", ""))
    )


class ProfileTestCase(TestCase):
    """The profile model test case."""

    def test_create_user_creates_profile(self):
        """Test that creating a user creates a profile."""
        user = UserFactory.create()
        self.assertEqual(user, Profile.objects.all().first().user)

    def test_all_profile_fields(self):
        """Test saving a profile exercising fields."""
        fake_bio = "Live long and prosper."
        fake_linked_in_url = "www.linkedin.com/in/all_the_spam"
        fake_repo_url = "www.github.com/bob"

        profile = UserFactory.create().profile
        profile.bio = fake_bio
        profile.linked_in_url = fake_linked_in_url
        profile.repo_url = fake_repo_url
        profile.save()

        test_profile = Profile.objects.first()
        self.assertEqual(test_profile.bio, fake_bio)
        self.assertEqual(test_profile.linked_in_url, fake_linked_in_url)
        self.assertEqual(test_profile.repo_url, fake_repo_url)


class MentorTestCase(TestCase):
    """Unit tests for the Mentor model."""

    def create_mentor(self):
        """Helper function to creat Mentor instances."""
        new_user = UserFactory.create()
        new_mentor = Mentor(profile=new_user.profile)
        new_mentor.save()
        return new_mentor

    def test_default_mentor_creation(self):
        """Test default values for newly created mentor."""
        new_mentor = self.create_mentor()

        self.assertEqual(new_mentor.area_of_expertise, "unknown")
        self.assertEqual(
            new_mentor.mentee_capacity,
            Mentor.DEFAULT_MENTEE_CAPACITY
        )
        self.assertFalse(new_mentor.currently_accepting_mentees)
        self.assertEqual(new_mentor.profile, User.objects.first().profile)

    def test_approved_mentor_manager(self):
        """Test that ApprovedMentorManager returns only approved mentors."""
        for _ in range(10):
            mentor = self.create_mentor()
            mentor.mentor_status = 'approved'
            mentor.save()

        for _ in range(10):
            mentor = self.create_mentor()
            # create 10 profiles with default mentor_status
            mentor.save()

        self.assertEqual(len(Mentor.objects.all()), 20)
        self.assertEqual(len(Mentor.approved_mentors.all()), 10)

    def test_pending_mentor_manager(self):
        """Test that PendingMentorManager returns only pending mentors."""
        for _ in range(10):
            mentor = self.create_mentor()
            mentor.mentor_status = 'pending'
            mentor.save()

        for _ in range(10):
            mentor = self.create_mentor()
            # create 10 profiles with default mentor_status
            mentor.save()

        self.assertEqual(len(Mentor.objects.all()), 20)
        self.assertEqual(len(Mentor.pending_mentors.all()), 10)


class MenteeTestCase(TestCase):
    """Unit tests for the Mentee model."""

    def create_mentee(self):
        """Helper function to create Mentees."""
        new_user = UserFactory.create()
        new_mentee = Mentee(profile=new_user.profile)
        new_mentee.save()
        return new_mentee

    def test_default_mentee_creation(self):
        """Test default values for newly created mentee."""
        new_mentee = self.create_mentee()

        self.assertEqual(new_mentee.area_of_interest, "unknown")
        self.assertEqual(new_mentee.profile, User.objects.first().profile)
