from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "gender",
    )
    search_fields = ("username",)
    list_filter = (
        "gender",
        "country",
    )
