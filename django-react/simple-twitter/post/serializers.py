from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """ Serializer for the post object"""

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "published_date",)

        read_only_fields = ("id", "published_date")