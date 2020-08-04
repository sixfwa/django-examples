from django.db import models
from django.conf import settings
from datetime import datetime


class Post(models.Model):
    """Post that a user creates"""
    content = models.TextField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
