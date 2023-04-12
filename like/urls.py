from django.urls import path
from .views import LikeAPIView, LikeDeleteView

urlpatterns = [
    path('<int:post_id>/like/', LikeAPIView.as_view(), name='post_like'),
    path('<int:pk>/unlike/', LikeDeleteView.as_view(), name='post_like'),

]
