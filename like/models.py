from django.db import models
from account.models import CustomUser
from post.models import Post


class Like(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'post']