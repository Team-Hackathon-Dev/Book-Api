from django.db import models
from account.models import CustomUser
from category.models import Category


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    owner = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='posts')
    pdf = models.FileField(upload_to='pdf/', null=True)
    images = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title[:50]}'

    class Meta:
        ordering = ('created_at',)
