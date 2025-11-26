from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import (
    TinyUserSerializer,
    UserDetailSerializer,
    MyUserProfileSerializer,
)
from tweets.serializers import TweetSerializer
from .models import CustomUser


class TinyUserInfoViews(APIView):
    def get(self, request):
        all_users = CustomUser.objects.all()
        serializer = TinyUserSerializer(all_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a user account with password
        CustomUser model > username 만 필수로 하고 있음
        > + with password
        """
        if request.data.get("password") is None:
            return Response(
                {"password": "This field is required."},
                status=400,
            )

        serializer = TinyUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get("password"))
            user.save()
            return Response(
                {
                    "data": serializer.data,
                    "message": "CustomUser Created Successfully with PASSWORD!",
                },
                status=200,
            )
        return Response(serializer.errors, status=400)


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


class UserDetailByUsernameViews(APIView):
    def get_object(self, username):
        try:
            return CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response(status=404)

    def get(self, request, username):
        user = self.get_object(username)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class MyUserProfileViews(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response(status=404)

    def get(self, request):
        user = self.get_object(request.user.pk)

        if request.user != user:
            return Response(
                {"detail": "You do not have permission to see other deep profile."},
                status=403,
            )

        serializer = MyUserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = self.get_object(request.user.pk)
        if request.user != user:
            return Response(
                {"detail": "You do not have permission to see other deep profile."},
                status=403,
            )

        serializer = MyUserProfileSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


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


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response(status=404)

    def put(self, request):
        user = self.get_object(request.user.pk)

        if request.user != user:
            return Response(
                {
                    "detail": "You do not have permission to change other user's password."
                },
                status=403,
            )

        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not user.check_password(old_password):
            return Response(
                {"old_password": "Wrong password."},
                status=400,
            )

        user.set_password(new_password)
        user.save()
        return Response({"detail": "Password updated successfully."})


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"detail": "Login successful."})
        else:
            return Response(
                {"detail": "Invalid credentials."},
                status=400,
            )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"detail": "Logout successful."})
