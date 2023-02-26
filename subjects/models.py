from django.db import models
import uuid

class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length= 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#  1 : 1 Com Teacher
    teacher = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="teacher")
