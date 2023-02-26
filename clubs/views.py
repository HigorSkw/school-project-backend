from .models import Club
from .serializers import ClubSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from users.permissions import IsTeacher, IsAdmin
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class ClubView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]

    serializer_class = ClubSerializer
    queryset = Club.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        return serializer.save()
    

class ClubDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly |IsAdmin ]

    serializer_class = ClubSerializer
    queryset = Club.objects.all()






    