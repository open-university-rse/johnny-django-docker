from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Website_activity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=200)
    

class Searches(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    text = models.TextField()