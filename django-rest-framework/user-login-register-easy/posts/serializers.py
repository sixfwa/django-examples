from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    user_email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Post
        fields = ('id', 'content', 'user_email', 'published')

        read_only_fields = ("id", "user", "published")
