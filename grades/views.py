from .models import Grade
from .serializers import GradeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from users.permissions import IsTeacher, IsAdmin
from django.shortcuts import get_object_or_404
from users.models import User
from subjects.models import Subject
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class GradeView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTeacher | IsAdmin ]

    serializer_class = GradeSerializer
    queryset = Grade.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        student_obj = get_object_or_404(
            User, pk=self.request.data["student"]
        )
        subject_obj = get_object_or_404(
            Subject, pk=self.request.data["subject"]
        )
        serializer.save(student=student_obj, subject=subject_obj)


class GradeDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTeacher | IsAdmin]

    serializer_class = GradeSerializer
    queryset = Grade.objects.all()