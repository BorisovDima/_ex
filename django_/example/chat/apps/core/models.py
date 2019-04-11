from django.db import models
from django.utils import timezone


class BaseChatModel(models.Model):

    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

