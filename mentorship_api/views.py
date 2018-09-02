from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from mentorship_profile.models import Profile, Mentor, Mentee
from mentorship_api.serializers import UserSerializer


class UserDetail(APIView):
    def get(self, request, format=None):
        user = request.user
        user.profile = Profile.objects.get(pk=user.profile.id)

        if (user.profile.is_mentor()):
            user.profile.mentor = Mentor.objects.get(pk=user.profile.mentor.id)

        if (user.profile.is_mentee()):
            user.profile.mentee = Mentee.objects.get(pk=user.profile.mentee.id)

        userSerializer = UserSerializer(user)
        return Response(userSerializer.data)
