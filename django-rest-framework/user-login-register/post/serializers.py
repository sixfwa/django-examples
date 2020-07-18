from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post object"""

    class Meta:
        model = Post
        fields = ("id", "content", "user")

        read_only_fields = ("id",)
