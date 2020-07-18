from django.db import models
from django.conf import settings


class Post(models.Model):
    """Post that a user creates"""
    content = models.TextField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.content
