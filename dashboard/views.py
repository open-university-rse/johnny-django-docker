from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import template
from files.models import Files


def countUserFiles(user):
    count = Files.objects.filter(user=user)
    return count.count()


# def home_dashboard(request):
#     users = User.objects.all()
#     data = []
#     for u in users:
#         userName = u.username
#         id = u.id
#         email = u.email
#         numFiles = countUserFiles(user=u)
#         data.append([{'username': userName, 'id': id, 'email': email, 'numFiles': numFiles}])

#     t = template.loader.get_template('dashboard.html')
#     print("data", data)
#     print("user", users)

#     html = t.render(data)
#     return HttpResponse(html)


def home_dashboard(request):
    users = User.objects.all()
    data = []

    for index, u in enumerate(users):
        numFiles = countUserFiles(user=u)
        di = {"name":u.username, "numfiles":numFiles }
        data.append(dict(di))

    t = template.loader.get_template("dashboard.html")
    html = t.render({'data': data})

    print({'data': data})
    
    return HttpResponse(html)

# def home_dashboard(request):
#     users = User.objects.all()
#     fileCounts = []
#     names = []

#     for u in users:
#         numFiles = countUserFiles(user=u)
#         fileCounts.append(numFiles)
#         names.append(u.username)
    
#     data = dict(zip(names, fileCounts))
#     t = template.loader.get_template("dashboard.html")
#     html = t.render(data)
#     print("data",data)
#     return HttpResponse(html)
