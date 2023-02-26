from django.urls import path
from .views import SubjectView

urlpatterns = [
    path('subjects/', SubjectView.as_view())
]