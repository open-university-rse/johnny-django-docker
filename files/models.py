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


def runProcess(commands):
    process = subprocess.run(
        commands,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    return process.stdout

def getBanditResult(fileName):
    commands = ["bandit", "-f", "json", fileName]
    stdout = runProcess(commands)
    return stdout


def getRadonResult(fileName):
    commands = ["radon", "raw", "-j", fileName]
    stdout = runProcess(commands)
    return stdout

def getVultureResult(fileName):
    commands = ["prospector", "--output-format", "json", "--strictness", "high", "--tool", "vulture",  fileName]
    stdout = runProcess(commands)
    return stdout

def getDodgyResult(fileName):
    commands = ["prospector", "--output-format", "json", "--strictness", "high", "--tool", "dodgy",  fileName]
    stdout = runProcess(commands)
    return stdout

def getPylintResult(fileName):
    commands = ["prospector", "--output-format", "json", "--strictness", "high", "--tool", "pylint",  fileName]
    stdout = runProcess(commands)
    return stdout

def getMcCabeResult(fileName):
    commands = ["prospector", "--output-format", "json", "--strictness", "high", "--tool", "mccabe",  fileName]
    stdout = runProcess(commands)
    return stdout




def createFileAndMetrics(user, time, text, path):
    # create file for bandit and radon
    filename = settings.TEST_DIR + "createFileAndMetrics.py"
    f = open(filename, "w")
    f.write(text)
    f.close()

    # so metrics
    bandit = getBanditResult(filename)
    radon = getRadonResult(filename)
    vulture = getVultureResult(filename)
    mccabe = getMcCabeResult(filename)
    pylint = getPylintResult(filename)
    dodgy = getDodgyResult(filename)

    print(mccabe)

    banditIssueString = []
    banditJson = json.loads(bandit)
    for result in banditJson["results"]:
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
    )

    return f
