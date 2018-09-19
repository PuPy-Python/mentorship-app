from rest_framework import serializers
from django.contrib.auth.models import User

from mentorship_profile.models import Profile, Mentor, Mentee
from mentorship_pairing.models import Pairing


class MentorSerializer(serializers.ModelSerializer):
    areas_of_interest = serializers.ListField()
    mentee_capacity = serializers.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = Mentor
        fields = ("id", "mentor_status", "areas_of_interest",
                  "mentee_capacity", "currently_accepting_mentees",
                  "approved_mentors", "available_mentors", "pending_mentors")


class MenteeSerializer(serializers.ModelSerializer):
    area_of_interest = serializers.CharField()
    goals = serializers.CharField()

    class Meta:
        model = Mentee
        fields = ("id", "area_of_interest", "goals")


class ProfileSerializer(serializers.ModelSerializer):
    slack_handle = serializers.CharField(required=False)
    linked_in_url = serializers.URLField(required=False)
    projects_url = serializers.URLField(required=False)
    bio = serializers.CharField(required=True)

    class Meta:
        model = Profile
        fields = ("id", "slack_handle", "linked_in_url", "projects_url", "bio",
                  "years_industry_experience", "email_confirmed")


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")


class PairingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pairing
        fields = ("id", "mentor", "mentee", "requested_by", "status",
                  "request_message")
