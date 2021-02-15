from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Website_activity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    startTime = models.DateTimeField(default=timezone.now)
    endTime = models.DateTimeField(default=timezone.now)
    history = models.JSONField(null=True)

class Searches(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    text = models.TextField()