from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import subprocess
import tempfile

# Create your models here.
class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    text = models.TextField(blank=True)
    path = models.TextField(blank=True)

    # metrics
    bandit = models.TextField(blank=True)
    bandit = models.JsonField(blank=True)
    loc = models.IntegerField(blank=True)
    lloc = models.IntegerField(blank=True)
    sloc = models.IntegerField(blank=True)
    comments = models.IntegerField(blank=True)
    multi = models.IntegerField(blank=True)
    blank = models.IntegerField(blank=True)
    singleComments = models.IntegerField(blank=True)

# class Metrics(models.Model):
#     file = models.ForeignKey(Files, on_delete=models.CASCADE)
#     time = models.DateTimeField(default=timezone.now)
#     bandit = models.TextField(blank=True)
#     loc = models.IntegerField(blank=True)
#     lloc = models.IntegerField(blank=True)
#     sloc = models.IntegerField(blank=True)
#     comments = models.IntegerField(blank=True)
#     multi = models.IntegerField(blank=True)
#     blank = models.IntegerField(blank=True)
#     singleComments = models.IntegerField(blank=True)

def getBanditResult(fileName):
    process = subprocess.run(
        ["bandit","-f", "json", fileName], stdout=subprocess.PIPE, universal_newlines=True
    )
    return process.stdout

def getRadonResult(fileName):
    process = subprocess.run(
        ["radon", "raw", "-j", fileName], stdout=subprocess.PIPE, universal_newlines=True
    )
    return process.stdout
