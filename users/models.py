from django.db import models
from django.contrib.auth.models import AbstractUser


class Gender(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
    OTHER = "other", "Other"


class Country(models.TextChoices):
    USA = (
        "usa",
        "USA",
    )
    KOREA = (
        "korea",
        "Korea",
    )


class CustomUser(AbstractUser):
    # nickname in twitter
    username = models.CharField(max_length=150, unique=True)

    country = models.CharField(
        max_length=20,
        choices=Country.choices,
        null=True,
        blank=True,
        default=Country.KOREA,
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        null=True,
        blank=True,
        default=Gender.OTHER,
    )
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    def __str__(self):
        return self.username
