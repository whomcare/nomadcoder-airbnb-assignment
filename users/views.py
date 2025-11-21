from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework.response import Response
from .serializers import TinyUserSerializer, UserDetailSerializer
from tweets.serializers import TweetSerializer
from .models import CustomUser


class TinyUserInfoViews(APIView):
    def get(self, request):
        all_users = CustomUser.objects.all()
        serializer = TinyUserSerializer(all_users, many=True)
        return Response(serializer.data)


class UserDetailViews(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class UserTweetsView(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = TweetSerializer(user.tweets.all(), many=True)

        return Response(serializer.data)
