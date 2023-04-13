from django.db import models
from account.models import CustomUser
from post.models import Post


class Comment(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} - {self.post}'
