from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Thread(models.Model):
    participants = models.ManyToManyField(User, related_name="threads")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
