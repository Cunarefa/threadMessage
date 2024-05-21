from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker


fake = Faker()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        users = []

        for _ in range(4):
            user = User(username=fake.unique.email(),
                        password=make_password(BaseUserManager().make_random_password()),
                        )

            users.append(user)

        User.objects.bulk_create(users)
