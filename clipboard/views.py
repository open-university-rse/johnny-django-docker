from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import UserSerializer, ClipboardSerializer, ClipboardGetSerializer
from .models import Clipboard
from django.contrib.auth.models import User
from rest_framework.views import Response, APIView
from django.http import HttpResponse
import datetime
from django import template

class ClipboardAPIViewSet(viewsets.ModelViewSet):
    serializer_class = ClipboardSerializer
    queryset = Clipboard.objects.all()
    def get(self, request, format=None):
        clip = clipboard.objects.all()
        serializer = ClipboardGetSerializer(clip)
        return Response(serializer.data)

    def post(self,request):
        serializer = ClipboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def clipboard(request):
    data = Clipboard.objects.all();
    t = template.loader.get_template('clipboard.html')
    html = t.render({'data': data})

    return HttpResponse(html)