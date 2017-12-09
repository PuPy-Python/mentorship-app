import factory
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile


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

    def test_create_profile_default_values(self):
        """Test a user profile is created with correct default values."""
        profile = UserFactory.create().profile

        self.assertEqual(profile.category, "unknown")
        self.assertEqual(profile.mentor_status, "unapproved")
        self.assertEqual(profile.currently_accepting_mentees, False)
        self.assertEqual(
            profile.mentee_capacity,
            Profile.DEFAULT_MENTEE_CAPACITY
        )

    def test_all_profile_fields(self):
        """Test saving a profile exercising fields."""
        profile = UserFactory.create().profile
        profile.bio = factory.Faker('text')
        profile.linked_in_url = factory.Faker('url')
        profile.repo_url = factory.Faker('url')
        profile.save()

    def test_approved_mentor_manager(self):
        """Test that ApprovedMentorManager returns only approved mentors."""
        for _ in range(10):
            profile = UserFactory.create().profile
            profile.mentor_status = 'approved'
            profile.save()

        for _ in range(10):
            profile = UserFactory.create().profile
            # create 10 profiles with default mentor_status
            profile.save()

        self.assertEqual(len(Profile.objects.all()), 20)
        self.assertEqual(len(Profile.approved_mentors.all()), 10)

    def test_pending_mentor_manager(self):
        """Test that PendingMentorManager returns only pending mentors."""
        for _ in range(10):
            profile = UserFactory.create().profile
            profile.mentor_status = 'pending'
            profile.save()

        for _ in range(10):
            profile = UserFactory.create().profile
            # create 10 profiles with default mentor_status
            profile.save()

        self.assertEqual(len(Profile.objects.all()), 20)
        self.assertEqual(len(Profile.pending_mentors.all()), 10)
