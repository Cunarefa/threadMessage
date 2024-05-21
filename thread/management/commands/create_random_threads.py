import random

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db.models import Q
from faker import Faker

from thread.models import Thread

fake = Faker()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        threads = []
        users = [user.id for user in User.objects.all()]

        for _ in range(6):
            thread = Thread()
            threads.append(thread)

        Thread.objects.bulk_create(threads)
        for thread in Thread.objects.all():
            participants = random.sample(users, k=2)
            if Thread.objects.filter(Q(participants__in=[participants[0]]) & Q(participants__in=[participants[1]])):
                continue
            thread.participants.set(participants)

