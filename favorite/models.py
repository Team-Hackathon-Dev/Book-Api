from django.db import models
from account.models import CustomUser
from post.models import Post


class Favorites(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'post']
