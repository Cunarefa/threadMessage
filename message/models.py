from django.contrib.auth.models import User
from django.db import models

from thread.models import Thread


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField(verbose_name="Text")
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="messages")
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


