from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
import subprocess
import tempfile
import json


# Create your models here.
class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    text = models.TextField(blank=True)
    path = models.TextField(blank=True)

    # metrics
    bandit = models.TextField(blank=True)
    banditIssues = models.TextField(blank=True)
    loc = models.IntegerField(blank=True)
    lloc = models.IntegerField(blank=True)
    sloc = models.IntegerField(blank=True)
    comments = models.IntegerField(blank=True)
    multi = models.IntegerField(blank=True)
    blank = models.IntegerField(blank=True)
    singleComments = models.IntegerField(blank=True)
    prospector = models.TextField(blank=True)


def getBanditResult(fileName):
    process = subprocess.run(
        ["bandit", "-f", "json", fileName],
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    return process.stdout


def getRadonResult(fileName):
    process = subprocess.run(
        ["radon", "raw", "-j", fileName],
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    return process.stdout


def getProspectorResult(fileName):
    process = subprocess.run(
        ["prospector", "--output-format", "json", "--without-tool", "bandit", fileName],
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    return process.stdout


def createFileAndMetrics(user, time, text, path):
    # create file for bandit and radon
    filename = settings.TEST_DIR + "createFileAndMetrics.py"
    f = open(filename, "w")
    f.write(text)
    f.close()

    # so metrics
    bandit = getBanditResult(filename)
    radon = getRadonResult(filename)
    prospector = getProspectorResult(filename)

    banditIssueString = []
    banditJson = json.loads(bandit)
    for result in banditJson["results"]:
        print(result["test_id"])
        banditIssueString.append(result["test_id"])


    # load radon json
    j = json.loads(radon)

    f = Files.objects.create(
        user=user,
        time=time,
        text=text,
        path=path,
        bandit=bandit,
        banditIssues=json.dumps(banditIssueString),
        loc=j[filename]["loc"],
        lloc=j[filename]["lloc"],
        sloc=j[filename]["sloc"],
        comments=j[filename]["comments"],
        multi=j[filename]["multi"],
        blank=j[filename]["blank"],
        singleComments=j[filename]["single_comments"],
        prospector=prospector,
    )

    return f
