from django.db import models
from account.models import CustomUser
from post.models import Post


class Like(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('owner', 'post')

