from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Clipboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    text = models.TextField(blank=True)
