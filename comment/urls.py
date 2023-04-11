from django.urls import path
from comment import views


urlpatterns = [
    path('comment/', views.CommentCreateView.as_view()),
    path('comment/<int:pk>/', views.CommentDetailView.as_view()),
]