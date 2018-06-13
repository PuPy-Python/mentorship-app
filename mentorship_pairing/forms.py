from django import forms
from mentorship_profile.models import Mentor, Mentee
from mentorship_pairing.models import Pairing


class PairingRequestForm(forms.ModelForm):
    """Form for requesting a Pairing."""

    request_message = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label="Request Message",
        help_text="Write a brief message to introduce yourself."
    )

    class Meta:
        model = Pairing
        fields = (
            "request_message",
        )
