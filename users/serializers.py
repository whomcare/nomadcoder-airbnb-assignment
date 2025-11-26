from rest_framework import serializers
from .models import CustomUser


class TinyUserSerializer(serializers.ModelSerializer):
    """
    for listing users
    """

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "avatar",
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    See other user's detailed information
    """

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "country",
            "gender",
            "bio",
            "avatar",
        ]


class MyUserProfileSerializer(serializers.ModelSerializer):
    """
    See MINE detailed information
    """

    written_tweets_count = serializers.IntegerField(
        source="tweets.count", read_only=True
    )

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "country",
            "gender",
            "bio",
            "birth_date",
            "avatar",
            "written_tweets_count",
        ]
        read_only_fields = ["username"]
