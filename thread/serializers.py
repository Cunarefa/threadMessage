from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers

from authentication.serializers import UserRegistrationSerializer
from thread.models import Thread


class ThreadSerializer(serializers.ModelSerializer):
    participants = UserRegistrationSerializer(read_only=True, many=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Thread
        fields = ("id", "created", "updated", "participants")

    def validate(self, data):
        participants = self.initial_data["participants"]
        if len(participants) != 2:
            raise ValueError("Only 2 participants can be assigned to the Thread.")
        return super().validate(data)

    def create(self, validated_data):
        participants = self.initial_data["participants"]
        thread = Thread.objects.filter(Q(participants__in=[participants[0]]) & Q(participants__in=[participants[1]]))

        if thread:
            return thread

        new_thread = Thread.objects.create(**validated_data)
        new_thread.participants.set(participants)
        return new_thread

