from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt import views

urlpatterns = [
    path('users/', UserView.as_view()),
    path("users/<uuid:pk>/", UserDetailView.as_view()),    
    path('users/login/', views.TokenObtainPairView.as_view()),
    path('users/login/refresh/', views.TokenRefreshView.as_view())
]