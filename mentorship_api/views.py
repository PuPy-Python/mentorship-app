from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from mentorship_profile.models import Profile, Mentor, Mentee
from mentorship_api.serializers import UserSerializer, ProfileSerializer, \
        MentorSerializer, MenteeSerializer


class UserDetail(APIView):
    def get(self, request, format=None):
        response = {}

        user = request.user
        userSerializer = UserSerializer(user)
        response["user"] = userSerializer.data

        profile = Profile.objects.get(pk=user.profile.id)
        profileSerializer = ProfileSerializer(profile)
        response["profile"] = profileSerializer.data

        if (profile.is_mentor()):
            mentor = Mentor.objects.get(pk=user.profile.mentor.id)
            mentorSerializer = MentorSerializer(mentor)
            response["mentor"] = mentorSerializer.data

        if (profile.is_mentee()):
            mentee = Mentee.objects.get(pk=user.profile.mentee.id)
            menteeSerializer = MenteeSerializer(mentee)
            response["mentee"] = menteeSerializer.data

        return Response(response)
