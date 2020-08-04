from django.db import models
from django.conf import settings


class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    published = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.content
