from django.urls import path
from .views import SubjectView, SubjectDetailView, SubjectSimpleView

urlpatterns = [
    path("subjects/", SubjectSimpleView.as_view()),
    path("subjects/teacher/<uuid:pk>/", SubjectView.as_view()),
    path("subjects/<uuid:pk>/", SubjectDetailView.as_view()),
]