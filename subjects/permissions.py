from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Subject


class IsAdminOrSubjectOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Subject):
        return request.user == obj.user or request.user.is_adm
