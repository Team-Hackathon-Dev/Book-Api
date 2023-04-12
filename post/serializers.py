from comment.serializers import CommentSerializer
from like.serializers import LikeSerializer
from rest_framework import serializers
from .models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    like_count = serializers.IntegerField(read_only=True)

    @staticmethod
    def is_liked(post, user):
        return user.likes.filter(post=post).exists()

    class Meta:
        model = Post
        fields = ['id', 'category', 'title', 'body', 'owner', 'like_count', 'created_at', 'updated_at', 'photo', 'pdf']

    def create(self, validated_data):
        return Post.objects.create(owner=self.context['request'].user, **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        # instance.photo = validated_data.get('photo', instance.photo)
        # instance.pdf = validated_data.get('pdf', instance.pdf)
        instance.save()
        return instance

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['likes_count'] = instance.likes.count()
        repr['liked_users'] = LikeSerializer(instance=instance.likes.all(), many=True).data
        repr['comments_count'] = instance.comments.count()
        repr['comments'] = CommentSerializer(instance=instance.comments.all(), many=True).data
        return repr

