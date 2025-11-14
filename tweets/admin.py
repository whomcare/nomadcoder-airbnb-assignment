from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("id", "payload", "user", "created_at", "updated_at")
    search_fields = ("payload", "user__nickname")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "tweet", "created_at", "updated_at")
