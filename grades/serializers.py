from rest_framework import serializers

from .models import Grade
from subjects.serializers import SubjectSerializer
from users.serializers import UserSerializer
from django.core.validators import MinValueValidator, MaxValueValidator


class GradeSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    note = serializers.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(10)])
    student = UserSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict) -> Grade:
        return Grade.objects.create(**validated_data)
    
    def update(self, instance: Grade, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
