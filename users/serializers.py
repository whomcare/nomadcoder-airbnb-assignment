from rest_framework import serializers
from .models import CustomUser


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "gender",
        ]
