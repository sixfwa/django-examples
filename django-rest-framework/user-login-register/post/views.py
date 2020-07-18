from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from post.models import Post
from post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Manage the posts in the database"""

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        if self.request.user.is_staff:
            return self.queryset
        else:

            queryset = self.queryset

            return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
