from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Post
from . import serializers
from .permissions import IsAuthorOrAdmin, IsAuthor


class DefaultResultPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = DefaultResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)
    filters_fields = ('owner', 'category')

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
