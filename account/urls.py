from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.UserListApiView.as_view()),
    path('register/', views.RegistrationView.as_view()),
    path('activate/<uuid:activation_code>', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('forgot/', views.ForgotPasswordView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]

#TODO CRUD
#TODO category
#TODO Post
#TODO title
#TODO descrip
#TODO image
#TODO book download
#TODO like
#TODO comment
#TODO permissions
