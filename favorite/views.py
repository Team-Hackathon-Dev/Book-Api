from rest_framework import generics, permissions
from favorite import serializers


class FavoriteCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)










