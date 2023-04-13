from django.db import models
from account.models import CustomUser
from category.models import Category


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    owner = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='posts')
    pdf = models.FileField(upload_to='pdf', null=True)
    photo = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title[:50]}'

    class Meta:
        ordering = ('created_at',)


class PostImages(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)

    def generate_name(self):
        from random import randint
        return 'image' + str(self.id) + str(randint(100000, 1_000_000))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(PostImages, self).save(*args, **kwargs)







