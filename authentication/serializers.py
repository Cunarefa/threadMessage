from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserRegistrationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=100, required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ("id", "username", "password")

    def create(self, data):
        user = User(username=data["username"])
        user.set_password(data["password"])
        user.save()
        return user
