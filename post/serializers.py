from category.models import Category
from comment.serializers import CommentSerializer
from like.serializers import LikeSerializer
from rest_framework import serializers
from .models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'price')

    def create(self, validated_data):
        request = self.context.get('request')
        post = Post.objects.create(**validated_data)
        return post


class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'price')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance


class PostListSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = ('id', 'title', 'category_name', 'owner_username', 'photo', 'price')

    @staticmethod
    def is_liked(post, user):
        return user.likes.filter(post=post).exists()

    @staticmethod
    def is_favorite(post, user):
        return user.favorites.filter(post=post).exists()

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['likes_count'] = instance.likes.count()
        repr['comments_count'] = instance.comments.count()
        user = self.context['request'].user
        if user.is_authenticated:
            repr['is_liked'] = self.is_liked(instance, user)
            repr['is_favorite'] = self.is_favorite(instance, user)
        return repr


class PostDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = '__all__'

    @staticmethod
    def is_liked(post, user):
        return user.likes.filter(post=post).exists()

    @staticmethod
    def is_favorite(post, user):
        return user.favorites.filter(post=post).exists()

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['likes_count'] = instance.likes.count()
        repr['liked_users'] = LikeSerializer(instance=instance.likes.all(), many=True).data
        repr['comments_count'] = instance.comments.count()
        repr['comments'] = CommentSerializer(instance=instance.comments.all(), many=True).data
        user = self.context['request'].user
        if user.is_authenticated:
            repr['is_liked'] = self.is_liked(instance, user)
            repr['is_favorite'] = self.is_favorite(instance, user)
        return repr
