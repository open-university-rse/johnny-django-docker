from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class VSCodeInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30)
    opened = models.DateTimeField(default=timezone.now)
    closed = models.DateTimeField(default=timezone.now)
