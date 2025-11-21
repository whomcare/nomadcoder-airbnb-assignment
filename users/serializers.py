from rest_framework import serializers
from .models import CustomUser


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "avatar",
        ]


class UserDetailSerializer(serializers.ModelSerializer):
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
        ]
