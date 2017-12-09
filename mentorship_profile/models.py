"""Module defines the User profile for the PuPPy Mentorship application."""
from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


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


class Profile(models.Model):
    """Definition of a user profile for the PuPPy Mentorship application."""

    # Categories for areas of interest / expertise
    CATEGORIES = (
        ("data science", "Data Science"),
        ("backend devops", "Back End / DevOps"),
        ("web full stack", "Web / Full Stack Development"),
        ("unknown", "Unknown")
    )

    MENTOR_STATUS = (
        ("approved", "Approved"),
        ("pending", "Pending"),
        ("unapproved", "Unapproved")
    )

    DEFAULT_MENTEE_CAPACITY = 5

    """
        The User model contains the following fields that will be used:

            username        str     Req
            password        str     Req
            first_name      str     Opt
            last_name       str     Opt
            email           str     Opt
            is_staff        bool    Opt

        Further details here:
        https://docs.djangoproject.com/en/1.11/ref/contrib/auth/
    """
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )

    mentor_status = models.CharField(
        default="unapproved",
        choices=MENTOR_STATUS,
        max_length=30
    )

    category = models.CharField(
        choices=CATEGORIES,
        max_length=30,
        default="unknown"
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
    repo_url = models.URLField(
        max_length=200,
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=False
    )

    goals = models.TextField(
        blank=False
    )

    # Use ForeignKey to allow option of having more than one mentor.
    mentors = models.ForeignKey(
        User,
        related_name="mentor_of",
        blank=True,
        null=True
    )

    # If an approved mentor, any profile can have many mentees.
    mentees = models.ForeignKey(
        User,
        related_name="mentored_by",
        blank=True,
        null=True
    )

    currently_accepting_mentees = models.BooleanField(
        default=False,
    )

    mentee_capacity = models.IntegerField(
        default=DEFAULT_MENTEE_CAPACITY
    )

    objects = models.Manager()

    approved_mentors = ApprovedMentorsManager()

    pending_mentors = PendingMentorsManager()


@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    """Ensure new profile created for every user."""
    if kwargs["created"]:
        new_profile = Profile(user=instance)
        new_profile.save()
