from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "password",
            "type_account",
            "is_adm",
            "created_at",
            "updated_at",
        ]

        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data: dict) -> User:
        
        return User.objects.create_superuser(**validated_data)


    def create(self, validated_data: dict) -> User:
        if "is_adm" not in validated_data or validated_data["is_adm"] is False:
            return User.objects.create_user(**validated_data)
        if validated_data["is_adm"] is True:
            return User.objects.create_superuser(**validated_data)
