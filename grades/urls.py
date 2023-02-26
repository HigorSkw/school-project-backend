from django.urls import path
from .views import GradeView, GradeDetailView

urlpatterns = [
    path('grades/', GradeView.as_view()),
    path("grades/<uuid:pk>/", GradeDetailView.as_view()),
]