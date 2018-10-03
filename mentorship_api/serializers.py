from rest_framework import serializers
from django.contrib.auth.models import User

from mentorship_profile.models import Profile, Mentor, Mentee


class MentorSerializer(serializers.ModelSerializer):
    areas_of_guidance = serializers.ListField()
    mentee_capacity = serializers.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = Mentor
        fields = ("id", "mentor_status", "areas_of_guidance",
                  "approved_mentors",
                  "available_mentors", "pending_mentors", "mentee_capacity",
                  "pending_mentors", "mentee_capacity",
                  "currently_accepting_mentees")


class MenteeSerializer(serializers.ModelSerializer):
    areas_of_guidance = serializers.ListField()
    goals = serializers.CharField()

    class Meta:
        model = Mentee
        fields = ("id", "areas_of_guidance", "goals")


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
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    def validate(self, data):
        password = data.get("password", None)
        confirm_password = data.pop("confirm_password", None)

        if not password:
            raise serializers.ValidationError(
                    "Password is required for signing up.")

        if not confirm_password:
            raise serializers.ValidationError(
                    "Password is required for signing up.")

        if password != confirm_password:
            raise serializers.ValidationError(
                    "Password and confirm password do not match.")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name",
                  "password", "confirm_password")
