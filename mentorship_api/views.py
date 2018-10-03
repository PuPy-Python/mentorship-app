from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from mentorship_profile.models import Profile, Mentor, Mentee
from mentorship_api.serializers import UserSerializer, ProfileSerializer, \
        MentorSerializer, MenteeSerializer


# https://stackoverflow.com/questions/405489/python-update-object-from-dictionary
def assign_dict(obj, updateDict):
    for key, value in updateDict.items():
        setattr(obj, key, value)


class UserCommon(APIView):
    def get(self, user):
        response = {}

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

    def put(self, user, jsonData):
        userData = jsonData.get("user", None)
        profileData = jsonData.get("profile", None)
        mentorData = jsonData.get("mentor", None)
        menteeData = jsonData.get("mentee", None)

        profile = Profile.objects.get(pk=user.profile.id)

        if userData:
            assign_dict(user, userData)
            user.save()

        if profileData:
            assign_dict(profile, profileData)
            profile.save()

        if mentorData and profile.is_mentor():
            mentor = Mentor.objects.get(pk=user.profile.mentor.id)
            assign_dict(mentor, mentorData)
            mentor.save()

        if menteeData and profile.is_mentee():
            mentee = Mentee.objects.get(pk=user.profile.mentee.id)
            assign_dict(mentee, menteeData)
            mentee.save()

        return Response(status=status.HTTP_200_OK)


class UserGeneral(UserCommon):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return super(UserGeneral, self).get(request.user)

    def put(self, request, format=None):
        jsonData = request.data
        return super(UserGeneral, self).put(request.user, jsonData)

    def post(self, request, format=None):
        jsonData = request.data

        userData = jsonData.get("user", None)
        profileData = jsonData.get("profile", None)
        mentorData = jsonData.get("mentor", None)
        menteeData = jsonData.get("mentee", None)

        userSerializer = UserSerializer(data=userData)
        profileSerializer = ProfileSerializer(data=profileData)
        mentorSerializer = None
        menteeSerializer = None

        if mentorData:
            mentorSerializer = MentorSerializer(data=mentorData)

        if menteeData:
            menteeSerializer = MenteeSerializer(data=menteeData)

        errors = None

        if not (userSerializer.is_valid()):
            errors = errors or {}
            errors["user"] = userSerializer.errors

        if not (profileSerializer.is_valid()):
            errors = errors or {}
            errors["profile"] = profileSerializer.errors

        if mentorSerializer and (not mentorSerializer.is_valid()):
            errors = errors or {}
            errors["mentor"] = mentorSerializer.errors

        if menteeSerializer and (not menteeSerializer.is_valid()):
            errors = errors or {}
            errors["mentee"] = menteeSerializer.errors

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {}

            user = userSerializer.save()
            response["user_id"] = userSerializer.data["id"]

            profileSerializer.instance = user.profile
            profile = profileSerializer.save()
            response["profile_id"] = profileSerializer.data["id"]

            if mentorSerializer:
                mentorSerializer.save(profile=profile)
                response["mentor_id"] = mentorSerializer.data["id"]

            if menteeSerializer:
                menteeSerializer.save(profile=profile)
                response["mentee_id"] = menteeSerializer.data["id"]

            return Response(response, status=status.HTTP_201_CREATED)


class UserDetail(UserCommon):
    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        return super(UserDetail, self).get(user)
