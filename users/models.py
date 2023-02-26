from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import uuid
from .manager import UserManager
from django.conf import settings


class typeOptions(models.TextChoices):
    TEACHER = "teacher"
    STUDENT = "student"
    ADMIN = "admin"


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    email = models.EmailField(unique=True, max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_account = models.CharField(max_length=20, choices=typeOptions.choices)
    is_adm = models.BooleanField(default=False, null=True, blank=True)
    USERNAME_FIELD = "email"

    objects = UserManager()

    USERNAME_FIELD = "email"

#  N : 1 - Club
    club = models.ForeignKey(
        "clubs.Club", on_delete=models.CASCADE, related_name="clubs", null=True
    )
