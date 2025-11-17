from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "payload",
        "user",
        "like_count",
        "created_at",
        "updated_at",
    )
    search_fields = ("payload", "user__nickname")

    def like_count(self, obj):
        return obj.likes.count()


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "tweet", "created_at", "updated_at")
