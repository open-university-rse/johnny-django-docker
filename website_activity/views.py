from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import UserSerializer, WebsiteActivitySerializer, SearchSerializer, WebsiteActivityGetSerializer
from .models import Website_activity, Searches
from django.contrib.auth.models import User
from rest_framework.views import Response, APIView
from django.http import HttpResponse
from django.template import loader

class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Searches.objects.all()

class WebsiteActivityViewSet(viewsets.ModelViewSet):
    serializer_class = WebsiteActivitySerializer
    queryset = Website_activity.objects.all()

class WebsiteActivityAPIViewSet(viewsets.ModelViewSet):
    serializer_class = WebsiteActivitySerializer
    queryset = Website_activity.objects.all()
    def get(self, request, format=None):
        webActivities = Website_activity.objects.all()
        serializer = WebsiteActivityGetSerializer(webActivities)
        return Response(serializer.data)

    def post(self,request):
        print("post: ",request.data )
        serializer = WebsiteActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def history(request):
    template = loader.get_template('history.html')
    return HttpResponse("Hello, world. You're at the history.")