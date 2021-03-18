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
            "numlinks": countUserWebsites(user=u)
        }
        data.append(dict(di))

    t = template.loader.get_template("dashboard.html")
    html = t.render({"data": data})

    return HttpResponse(html)

def user_dashboard(request, user_id):
    users = User.objects.all(id=user_id)
    
    t = template.loader.get_template("user_dashboard.html")
    html = t.render({"user_id": user_id})

    return HttpResponse(html)
