from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
