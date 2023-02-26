from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdmin, IsAuthenticatedOrPost, IsStudent, IsTeacher, IsAccountOwner
from rest_framework.views import Response, status


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrPost]


    def get_queryset(self):
        if self.request.user.is_adm:
            return self.queryset.all()

        return self.queryset.filter(email=self.request.user.email)

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner | IsAdmin]

    def patch(self, request, *args, **kwargs):

        if "is_adm" in request.data:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )

        return self.partial_update(request, *args, **kwargs)
