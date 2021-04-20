from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import template
from files.models import Files
from clipboard.models import Clipboard
from website_activity.models import Website_activity


def countUserFiles(user):
    count = Files.objects.filter(user=user)
    return count.count()


def countUserClipboards(user):
    count = Clipboard.objects.filter(user=user)
    return count.count()


def countUserWebsites(user):
    count = Website_activity.objects.filter(user=user)
    return count.count()


def home_dashboard(request):
    users = User.objects.all()
    data = []

    for index, u in enumerate(users):
        numFiles = countUserFiles(user=u)
        di = {
            "name": u.username,
            "id": u.id,
            "numfiles": countUserFiles(user=u),
            "numclips": countUserClipboards(user=u),
            "numlinks": countUserWebsites(user=u),
        }
        data.append(dict(di))

    t = template.loader.get_template("dashboard.html")
    html = t.render({"data": data})

    return HttpResponse(html)


def user_dashboard(request, username):
    user = User.objects.get(username=username)
    files = Files.objects.filter(user=user)
    clipboards = Clipboard.objects.filter(user=user)
    webs = Website_activity.objects.filter(user=user)

    t = template.loader.get_template("user_dashboard.html")
    html = t.render(
        {"username": user, "files": files, "clipboards": clipboards, "webs": webs}
    )
    return HttpResponse(html)


def user_history_dashboard(request, username):
    user = User.objects.get(username=username)
    files = Files.objects.filter(user=user)
    clipboards = Clipboard.objects.filter(user=user)
    webs = Website_activity.objects.filter(user=user)

    # create events dictionary and populate
    data = []
    for file in files:
        event = {
            "time": file.time,
            "type": "File",
            "info": file.text,
        }
        data.append(dict(event))
    
    for clip in clipboards:
        event = {
            "time": clip.time,
            "type": "Paste",
            "info": clip.text,
        }
        data.append(dict(event))

    for web in webs:
        event = {
            "time": web.time,
            "type": "Website",
            "info": web.url,
        }
        data.append(dict(event))
    # sort into date order 
    data.sort(key=lambda e: e['time'])

    t = template.loader.get_template("user_history_dashboard.html")
    html = t.render({"data": data, "username": username})

    return HttpResponse(html)

def userFilesDashboard(request, username):
    user = User.objects.get(username=username)
    files = Files.objects.filter(user=user)

    metrics = []
    for file in files:
        event = {
            "bandit": file.bandit,
            "mccabe": file.mccabe,
            "dodgy": file.dodgy,
            "vulture": file.vulture,
            "pylint": file.pylint,
        }
        metrics.append(dict(event))
    
    t = template.loader.get_template("user_files_dashboard.html")
    html = t.render(
        {"username": username, "files": files, "metrics": metrics}
    )
    return HttpResponse(html)

def userWebsDashboard(request, username):
    user = User.objects.get(username=username)
    webs = Website_activity.objects.filter(user=user)
    
    t = template.loader.get_template("user_web_dashboard.html")
    html = t.render(
        {"username": username, "webs": webs}
    )
    return HttpResponse(html)

def userClipboardsDashboard(request, username):
    user = User.objects.get(username=username)
    clipboards = Clipboard.objects.filter(user=user)
    
    t = template.loader.get_template("user_clipboards_dashboard.html")
    html = t.render(
        {"username": username, "clipboards": clipboards}
    )
    return HttpResponse(html)

