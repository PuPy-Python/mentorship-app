from rest_framework import serializers
from django.contrib.auth.models import User

from mentorship_profile.models import Profile, Mentor, Mentee


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ("id", "mentor_status", "areas_of_interest",
                  "approved_mentors",
                  "available_mentors", "pending_mentors", "mentee_capacity",
                  "pending_mentors", "mentee_capacity",
                  "currently_accepting_mentees")


class MenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentee
        fields = ("id", "area_of_interest", "goals")


class ProfileSerializer(serializers.ModelSerializer):
    mentor = MentorSerializer()
    mentee = MenteeSerializer()

    class Meta:
        model = Profile
        fields = ("id", "slack_handle", "linked_in_url", "projects_url", "bio",
                  "years_industry_experience", "email_confirmed",
                  "mentor", "mentee")


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name",
                  "profile")
