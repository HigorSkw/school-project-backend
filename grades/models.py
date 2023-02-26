from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class Grade(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    note = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 1:1 - Subject 

    subject = models.OneToOneField("subjects.Subject", on_delete=models.CASCADE)
    
    #  N : 1 - Student
    student = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="students"
    )
