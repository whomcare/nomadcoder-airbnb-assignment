from django.db import models
from django.contrib.auth.models import AbstractUser


class Gender(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
    OTHER = "other", "Other"


class CustomUser(AbstractUser):
    # nickname in twitter
    username = models.CharField(max_length=150, unique=True)
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        null=True,
        blank=True,
        default=Gender.OTHER,
    )

    def __str__(self):
        return self.username
