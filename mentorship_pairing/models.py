from django.db import models

# Create your models here.
from mentorship_profile.models import (Mentee, Mentor)


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
        # TODO: Just Delete?
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

    status = models.CharField(
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
