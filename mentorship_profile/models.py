"""Module defines the User profile for the PuPPy Mentorship application."""
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from multiselectfield import MultiSelectField

CATEGORIES = (
    ("data science", "Data Science"),
    ("backend devops", "Back End / DevOps"),
    ("web full stack", "Web / Full Stack Development"),
    ("unknown", "Unknown")
)

AREAS_OF_GUIDANCE = (
        ('portfolio_code_review', 'Portfolio / Code Reviews'),
        ('job_search_interviews', 'Job Search and Interviews'),
        ('industry_trends', 'Industry Trends, Skills, Technologies'),
        ('leadership_management', 'Leadership / Management'),
        ('business_entrepreneurship', 'Business, Entrepreneurship'),
        ('career_growth', 'Career Growth'),
    )

YEARS = (
    ("0-1", "0 - 1"),
    ("1-3", "1 - 3"),
    ("3-7", "3 - 7"),
    ("7+", "7 +")
)


class Profile(models.Model):
    """Definition of a user profile for the PuPPy Mentorship application."""

    """
        The User model contains the following fields that will be used:

            username        str     Req
            password        str     Req
            first_name      str     Opt
            last_name       str     Opt
            email           str     Opt
            is_staff        bool    Opt
            is_active       bool    Opt

        Further details here:
        https://docs.djangoproject.com/en/1.11/ref/contrib/auth/
    """
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )

    slack_handle = models.CharField(
        max_length=40,
        blank=True,
        null=True
    )

    linked_in_url = models.URLField(
        max_length=200,
        blank=True,
        null=True
    )

    # Url for github/gitlab/bitbucket account
    projects_url = models.URLField(
        max_length=200,
        blank=True,
        null=True
    )

    bio = models.TextField(
        max_length=500,
        blank=False
    )

    years_industry_experience = models.CharField(
        choices=YEARS,
        max_length=3,
        default="0-1"
    )

    email_confirmed = models.BooleanField(default=False)

    objects = models.Manager()

    def is_mentor(self):
        """Whether or not current user is a mentor."""
        try:
            self.mentor
            return True
        except ObjectDoesNotExist:
            return False

    def is_mentee(self):
        """Whether or not current user is a mentee."""
        try:
            self.mentee
            return True
        except ObjectDoesNotExist:
            return False


@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    """Ensure new profile created for every user."""
    if kwargs["created"]:
        new_profile = Profile(user=instance)
        new_profile.save()


class ApprovedMentorsManager(models.Manager):
    """Return the set of approved Mentors."""

    def get_queryset(self):
        """Overwrite to return only approved Mentors."""
        return super(ApprovedMentorsManager, self).get_queryset()\
            .filter(mentor_status="approved").all()


class AvailableMentorsManager(models.Manager):
    """Return the set of available Mentors."""

    def get_queryset(self):
        return super(AvailableMentorsManager, self).get_queryset()\
            .filter(mentor_status="approved")\
            .filter(currently_accepting_mentees=True)
# TODO: Return Mentors who have less than max allowed mentees.


class PendingMentorsManager(models.Manager):
    """Return the set of pending Mentors."""

    def get_queryset(self):
        """Overwrite to return only pending Mentors."""
        return super(PendingMentorsManager, self).get_queryset()\
            .filter(mentor_status="pending").all()


class Mentor(models.Model):
    """Define a table for tracking mentors."""

    MENTOR_STATUS_CHOICES = (
        ("approved", "Approved"),
        ("pending", "Pending"),
        ("unapproved", "Unapproved")
    )

    DEFAULT_MENTEE_CAPACITY = 5

    profile = models.OneToOneField(
        Profile
    )

    mentor_status = models.CharField(
        choices=MENTOR_STATUS_CHOICES,
        max_length=30,
        default="unapproved"
    )

    areas_of_guidance = MultiSelectField(
        choices=AREAS_OF_GUIDANCE,
        max_length=130,
        default="unknown"
    )

    approved_mentors = ApprovedMentorsManager()

    available_mentors = AvailableMentorsManager()

    pending_mentors = PendingMentorsManager()

    mentee_capacity = models.IntegerField(
        default=DEFAULT_MENTEE_CAPACITY
    )

    currently_accepting_mentees = models.BooleanField(
        default=False,
    )

    objects = models.Manager()


class Mentee(models.Model):
    """Define a table for tracking mentees."""

    profile = models.OneToOneField(
        Profile
    )

    areas_of_guidance = MultiSelectField(
        choices=AREAS_OF_GUIDANCE,
        max_length=130,
        default="unknown"
    )

    goals = models.TextField(
        blank=False
    )

    objects = models.Manager()
