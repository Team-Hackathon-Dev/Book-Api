from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryCreateListView.as_view()),
    path('category/<int:pk>/', views.CategoryDetailView.as_view()),
]