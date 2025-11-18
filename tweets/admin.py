from django.contrib import admin
from .models import Tweet, Like


class ElonMuskFilter(admin.SimpleListFilter):
    title = "Elon Musk NomadCoder"
    parameter_name = "elon_musk"

    def lookups(self, request, model_admin):
        return (
            ("contains", "Contains Elon Musk"),
            ("not_contains", "Doesn't Contain Elon Musk"),
        )

    def queryset(self, request, queryset):
        value = self.value()

        if value == "contains":
            # 대소문자 무시하고 "elon musk" 포함
            return queryset.filter(payload__icontains="elon musk")

        if value == "not_contains":
            return queryset.exclude(payload__icontains="elon musk")

        return queryset


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    # Filter by created_at (2025.11.18 assignment)
    list_display = (
        "id",
        "payload",
        "user",
        "like_count",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "created_at",  # 날짜 필터
        ElonMuskFilter,
    )

    # Search by payload, username of user foreign key. (2025.11.18 assignment)
    search_fields = (
        "payload",
        "user__username",
    )

    @admin.display(description="Likes")
    def like_count(self, obj):
        return obj.likes.count()


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    # Filter by created_at (2025.11.18 assignment)
    list_display = (
        "id",
        "user",
        "tweet",
        "created_at",
        "updated_at",
    )

    list_filter = ("created_at",)

    # Search by username of user foreign key (2025.11.18 assignment)
    search_fields = ("user__username",)
