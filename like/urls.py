from django.urls import path
from like import views

urlpatterns = [
    path('', views.LikeCreateView.as_view()),
    path('<int:pk>/', views.LikeDeleteView.as_view()),
    path('list/', views.LikeListView.as_view()),
]
