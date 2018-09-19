from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from mentorship_profile.models import Profile, Mentor, Mentee
from mentorship_pairing.models import Pairing
from mentorship_api.serializers import UserSerializer, ProfileSerializer, \
        MentorSerializer, MenteeSerializer, PairingSerializer


class UserDetail(APIView):
    permission_classes = (AllowAny,)

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

    def post(self, request, format=None):
        jsonData = request.data

        userData = jsonData["user"]
        profileData = jsonData["profile"]
        mentorData = jsonData["mentor"]
        menteeData = jsonData["mentee"]

        userSerializer = UserSerializer(data=userData)
        profileSerializer = ProfileSerializer(data=profileData)
        mentorSerializer = MentorSerializer(data=mentorData)
        menteeSerializer = MenteeSerializer(data=menteeData)

        errors = None

        if not (userSerializer.is_valid()):
            errors = errors or {}
            errors["user"] = userSerializer.errors

        if not (profileSerializer.is_valid()):
            errors = errors or {}
            errors["profile"] = profileSerializer.errors

        if not (mentorSerializer.is_valid()):
            errors = errors or {}
            errors["mentor"] = mentorSerializer.errors

        if not (menteeSerializer.is_valid()):
            errors = errors or {}
            errors["mentee"] = menteeSerializer.errors

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = userSerializer.save()

            profileSerializer.instance = user.profile
            profile = profileSerializer.save()

            mentorSerializer.save(profile=profile)
            menteeSerializer.save(profile=profile)

            response = {}
            response["user_id"] = userSerializer.data["id"]
            response["profile_id"] = profileSerializer.data["id"]
            response["mentor_id"] = mentorSerializer.data["id"]
            response["mentee_id"] = menteeSerializer.data["id"]
            return Response(response, status=status.HTTP_201_CREATED)


class PairingList(generics.ListCreateAPIView):
    # TODO: instead of mentor id and mentee id,
    #       should use mentor's and mentee's user ids
    queryset = Pairing.objects.all()
    serializer_class = PairingSerializer


class PairingDetail(generics.RetrieveUpdateDestroyAPIView):
    # TODO: instead of mentor id and mentee id,
    #       should use mentor's and mentee's user ids
    queryset = Pairing.objects.all()
    serializer_class = PairingSerializer
