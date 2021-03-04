from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import template
    
def home_dashboard(request):
    data = User.objects.all();
    t = template.loader.get_template('dashboard.html')
    html = t.render({'data': data})

    return HttpResponse(html)