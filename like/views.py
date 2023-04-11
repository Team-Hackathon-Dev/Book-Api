from rest_framework import generics, permissions
from rest_framework.response import Response
from like.models import Like
from like.serializers import LikeSerializer
from post.models import Post
from post.permissions import IsAuthor


class LikeAPIView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(pk=post_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, post=post)

        return Response(serializer.data)


class LikeDeleteView(generics.DestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]
    queryset = Like.objects.all()


