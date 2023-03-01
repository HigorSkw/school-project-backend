from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Subject
from users.models import User
from .serializers import SubjectSerializer
from users.permissions import IsAdmin, IsTeacher
from django.shortcuts import get_object_or_404
from rest_framework.views import Response, status


class SubjectSimpleView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_adm:
            return self.queryset.all()

        return self.queryset.filter(email=self.request.user.email)


class SubjectView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [ IsTeacher | IsAdmin]

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        teacher_obj = get_object_or_404(User, pk=self.kwargs.get('pk'))

        if (teacher_obj.type_account != "teacher"):
            return Response(
                {"message": "Invalid user type"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return serializer.save(teacher=teacher_obj)


class SubjectDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()