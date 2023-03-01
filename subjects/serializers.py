from rest_framework import serializers
from .models import Subject
from users.serializers import UserSerializer


class SubjectSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)

    class Meta:
        model = Subject
        fields =[
            "id",
            "name",
            "created_at",
            "updated_at",
            "teacher"
        ]
        depth = 1

        read_only_fields = ["id", "created_at", "updated_at", "teacher"]