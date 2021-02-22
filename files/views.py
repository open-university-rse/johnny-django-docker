
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import  FilesPostSerializer, FilesGetSerializer
from .models import Files
from django.contrib.auth.models import User
from rest_framework.views import Response, APIView
from django.http import HttpResponse
import datetime
from django import template
# Create your views here.

class FilesAPIViewSet(viewsets.ModelViewSet):
    serializer_class = FilesGetSerializer
    queryset = Files.objects.all()
    def get(self, request, format=None):
        webActivities = Files.objects.all()
        serializer = FilesGetSerializer(webActivities)
        return Response(serializer.data)

    def post(self,request):
        print("post: ",request.data )
        serializer = FilesPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def files(request):
    data = Files.objects.all();
    t = template.loader.get_template('files.html')
    html = t.render({'data': data})

    return HttpResponse(html)