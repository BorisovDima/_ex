from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    about_me = models.CharField(max_length=124, null=True, blank=True)
    last_activity = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='', null=True, blank=True)
    last_seen = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'user-{self.id}'
