from django.db import models
import uuid

class typeOptions(models.TextChoices):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    NIGHT = "night"

# Create your models here.
class Club(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    year = models.PositiveIntegerField()
    shift = models.CharField(max_length=20, choices=typeOptions.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#  N : N - Subjects
    subjects = models.ManyToManyField("subjects.Subject", related_name="subjects")

    