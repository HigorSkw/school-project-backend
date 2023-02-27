from rest_framework import serializers
from .models import Club, typeOptions
from subjects.models import Subject


class ClubSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    year = serializers.CharField()
    shift = serializers.ChoiceField(
        choices=typeOptions.choices
    )
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    subjects = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True)

    def create(self, validated_data: dict) -> Club:
        subjects_data = validated_data.pop('subjects')
        newClub = Club.objects.create(**validated_data)
        newClub.subjects.set(subjects_data)
        return newClub
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.year = validated_data.get("year", instance.year)
        instance.shift = validated_data.get("shift", instance.shift)
        subjects_data = validated_data.pop("subjects", None)
        if subjects_data is not None:
            instance.subjects.set(subjects_data)
        instance.save()
        return instance
