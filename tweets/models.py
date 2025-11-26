from django.db import models
from common.models import Common
from users.models import CustomUser


class LikeType(models.TextChoices):
    TWEET = ["Tweet", "tweet"]
    COMMENT = ["Comment", "comment"]


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


class Comment(Common):
    payload = models.TextField(max_length=200)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        related_name="comments",
    )

    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        null=False,
        related_name="comments",
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
        null=True,
        related_name="likes",
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        null=True,
        related_name="likes",
    )
    like_type = models.CharField(
        max_length=20,
        null=False,
        blank=True,
        choices=LikeType.choices,
        default=LikeType.TWEET,
    )

    def __str__(self):
        if self.like_type == LikeType.COMMENT:
            return f"{self.user} likes {self.comment}"
        else:
            return f"{self.user} likes {self.tweet}"
