from django.urls import path
from .views import ClubView, ClubDetailView

urlpatterns = [
    path('clubs/', ClubView.as_view()),
    path('clubs/<uuid:pk>/', ClubDetailView.as_view())
]