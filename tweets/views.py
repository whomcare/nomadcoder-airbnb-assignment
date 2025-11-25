from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound, PermissionDenied
from .serializers import TweetSerializer, TweetDetailSerializer
from .models import Tweet


class TweetListView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all().order_by("-created_at")
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request):  # 251125_assignment > Success
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class TweetDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetDetailSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk):  # 251125_assignment > Success
        tweet = self.get_object(pk)

        if tweet.user != request.user:
            raise PermissionDenied

        serializer = TweetDetailSerializer(tweet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):  # 251125_assignment > Success
        tweet = self.get_object(pk)

        if tweet.user != request.user:
            raise PermissionDenied

        tweet.delete()
        return Response(status=204)
