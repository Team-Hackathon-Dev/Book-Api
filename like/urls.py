from django.urls import path
from .views import LikeAPIView, LikeDeleteView

urlpatterns = [
    path('post/<int:post_id>/like/', LikeAPIView.as_view(), name='post_like'),
    path('post/<int:pk>/unlike/', LikeDeleteView.as_view(), name='post_like'),

]
