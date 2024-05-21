from rest_framework import serializers

from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=False)
    is_read = serializers.BooleanField(default=False)

    class Meta:
        model = Message
        read_only_fields = ("sender", "created", "is_read", "thread")
        fields = read_only_fields + ("id", "text")

