from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    text = models.TextField(blank=True)
    path = models.TextField(blank=True)

class Metrics(models.Model):
    file = models.ForeignKey(Files, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    bandit = models.TextField(blank=True)

# def calculateMetrics(fileName):
    
