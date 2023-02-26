from django.urls import path
from .views import GradeView

urlpatterns = [
    path('grades/', GradeView.as_view())
]