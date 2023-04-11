from rest_framework import generics, permissions
from post.permissions import IsAuthorOrAdminOrPostOwner
from .models import Comment
from . import serializers
from .serializers import CommentSerializer


class CommentCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializers_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == 'Destroy':
            return IsAuthorOrAdminOrPostOwner(),
        return permissions.AllowAny(),
