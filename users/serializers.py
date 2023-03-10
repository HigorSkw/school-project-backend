from rest_framework import serializers
from .models import User, typeOptions


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
            "club"
        ]

        depth = 1

        type_account = serializers.ChoiceField(
            choices=typeOptions.choices
        )

        read_only_fields = ["id", "created_at", "updated_at", "club"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        if validated_data["type_account"] == "admin":
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)
        
