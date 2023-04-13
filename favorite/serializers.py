from rest_framework import serializers
from favorite.models import Favorites


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorites
        fields = ['post', 'owner', 'owner_username', 'created_date']

    def validate(self, attrs):
        request = self.context['request']
        user = request.user
        post = attrs['post']
        if user.favorites.filter(post=post).exists():
            favorite = user.favorites.filter(post=post)
            favorite.delete()
            raise serializers.ValidationError('Deleted from favorites!')
        return attrs
