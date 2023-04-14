from rest_framework import viewsets, permissions, status
from rest_framework.viewsets import ModelViewSet
from .models import Post
from . import serializers
from .permissions import IsAuthorOrAdmin, IsAuthor


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PostListSerializer
        elif self.action in 'create':
            return serializers.PostCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return serializers.PostUpdateSerializer
        return serializers.PostDetailSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.IsAuthenticated(), IsAuthorOrAdmin()]
        elif self.action in ('update', 'partial_update'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        return [permissions.IsAuthenticatedOrReadOnly()]
