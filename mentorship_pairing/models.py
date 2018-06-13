from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from mentorship_profile.models import (Mentee, Mentor, Profile)


# TODO: Different reasons for Mentor/Mentee?
DISCONTINUE_REASONS = (
    "Personal Reasons",
    "No longer needed",
    "No longer have time",
)

MENTOR_REJECT_PAIRING_REASONS = (
    "Unavailable",
    "Not a good fit."
)

MENTEE_REJECT_PAIRING_REASONS = (
    "Not a good fit.",
    "Want somebody with more experience."
)


class ActivePairingsManager(models.Manager):
    """Return the set of approved Mentors."""

    def get_queryset(self):
        """Overwrite to return only active Pairings."""
        return super(ActivePairingsManager, self).get_queryset()\
            .filter(status="active").all()


class PendingPairingsManager(models.Manager):
    """Return the set of pending pairings."""

    def get_queryset(self):
        """Overwrite to return only pending Mentors."""
        return super(PendingPairingsManager, self).get_queryset()\
            .filter(status="pending").all()


class Pairing(models.Model):
    """Definition of a Pairing between a Mentor and Mentee."""

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("active", "Active"),
        ("rejected", "Rejected"),
        ("discontinued", "Discontinued")
    )

    mentor = models.OneToOneField(
        Mentor,
        related_name="pairing",
        on_delete=models.CASCADE
    )

    mentee = models.OneToOneField(
        Mentee,
        related_name="pairing",
        on_delete=models.CASCADE
    )

    requested_by = models.ForeignKey(
        Profile,
        related_name="requested_pairing",
        null=True,
        blank=True
    )

    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=40,
        blank=False,
        null=False,
        default="pending"
    )

    request_message = models.TextField(
        blank=True
    )

    date_created = models.DateTimeField(
        auto_now_add=True
    )

    date_modified = models.DateTimeField(
        auto_now=True
    )

    active_pairings = ActivePairingsManager()

    pending_pairings = PendingPairingsManager()

    objects = models.Manager()

    def save(self, *args, **kwargs):
        """
        Overwrite save method.

        We want to prevent saving a Pairing if a mentor and mentee are the same
        user.
        """

        if self.mentor.profile is self.mentee.profile:
            raise ValidationError("Mentor and Mentee cannot be same user.")
        else:
            super(Pairing, self).save(*args, **kwargs)

    def is_user_in_pairing(self, user):
        """Return whether or not the given user is in the pairing."""
        return user in (self.mentor.profile.user, self.mentee.profile.user)

    @property
    def requestor(self):
        """Return the profile that initiated this pairing."""
        return self.requested_by

    @property
    def requestee(self):
        """Return the profile that is requested to join this pairing."""
        if self.requested_by is None:
            # We don't know, return None
            return None
        elif self.requested_by is self.mentee.profile:
            return self.mentor.profile
        return self.mentee.profile
