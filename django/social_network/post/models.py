from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """A model for a status update"""
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
