"""Module defines the User profile for the PuPPy Mentorship application."""
from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

CATEGORIES = (
    ("data science", "Data Science"),
    ("backend devops", "Back End / DevOps"),
    ("web full stack", "Web / Full Stack Development"),
    ("unknown", "Unknown")
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
        blank=False
    )

    email_confirmed = models.BooleanField(default=False)

    objects = models.Manager()


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
        default="unapproved",
        choices=MENTOR_STATUS_CHOICES,
        max_length=30
    )

    area_of_expertise = models.CharField(
        choices=CATEGORIES,
        max_length=30,
        default="unknown"
    )

    approved_mentors = ApprovedMentorsManager()

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

    area_of_interest = models.CharField(
        choices=CATEGORIES,
        max_length=30,
        default="unknown"
    )

    goals = models.TextField(
        blank=False
    )

    objects = models.Manager()
