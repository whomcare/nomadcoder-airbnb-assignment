from django.db import models
from common.models import Common
from users.models import CustomUser


# The tweets app should have the models: Tweet and Like.
class Tweet(Common):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        related_name="tweets",
    )

    def __str__(self):
        return self.payload


class Like(Common):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        related_name="likes",
    )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        null=False,
        related_name="likes",
    )

    def __str__(self):
        return f"{self.user} likes {self.tweet}"
