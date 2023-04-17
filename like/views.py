from rest_framework import generics, permissions
from like import serializers
from like.models import Like
from like.serializers import LikeSerializer, LikeListSerializer
from post.permissions import IsAuthor


class LikeCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer


class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthor)










