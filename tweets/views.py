from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TweetSerializer
from .models import Tweet


class TweetListView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all().order_by("-created_at")
        serializer = TweetSerializer(tweets, many=True)

        return Response(serializer.data)


class TweetDetailView(APIView):
    def get(self, request, pk):
        tweet = Tweet.objects.get(pk=pk)
        serializer = TweetSerializer(tweet)

        return Response(serializer.data)
