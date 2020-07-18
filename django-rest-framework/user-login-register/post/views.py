from rest_framework import viewsets

from post.models import Post
from post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Manage the posts in the database"""

    serializer_class = PostSerializer
    queryset = Post.objects.all()
