from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post object"""

    user_email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Post
        fields = ("id", "content", "user_email")

        read_only_fields = ("id", "user_email")
