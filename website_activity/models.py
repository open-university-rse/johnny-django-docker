from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Website_activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=200)
    title = models.TextField(blank=True)
    
