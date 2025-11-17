from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            "id",
            "payload",
            "user",
            "created_at",
            "updated_at",
            "like_count",
        ]

    def get_like_count(self, obj):
        return obj.likes.count()
