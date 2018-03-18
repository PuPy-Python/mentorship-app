from django import forms
from .mentorship_profile.models import Mentor, Mentee
from .mentorship_pairing.models import Pairing


# class RequestPairingForm(forms.ModelForm):

#     mentor = forms.ModelChoiceField(
#         queryset=Mentor.objects.all()
#     )

#     mentee = forms.ModelChoiceField(
#         queryset=Mentee.objects.all()
#     )

#     class Meta:
#         model = Pairing
#         fields = (
#             "mentor",
#             "mentee",
#             "request_message"
#         )
