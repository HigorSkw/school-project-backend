from django.db import models
import uuid

class Grade(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    note = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 1:1 - Subject 

    subject = models.OneToOneField("subjects.Subject", on_delete=models.CASCADE)
    
    #  N : 1 - Student
    student = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="students"
    )
