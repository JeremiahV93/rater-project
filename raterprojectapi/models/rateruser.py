from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE


class Rateruser(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=50)
