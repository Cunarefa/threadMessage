import random

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker

from message.models import Message
from thread.models import Thread

fake = Faker()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        messages = []
        users = User.objects.all()
        threads = Thread.objects.all()

        for user in users:
            for _ in range(4):
                thread = Thread.objects.get(id=random.choice(threads).id)
                message = Message(
                    thread=thread,
                    text=fake.text(max_nb_chars=150),
                    sender=user
                )

                messages.append(message)

        Message.objects.bulk_create(messages)
