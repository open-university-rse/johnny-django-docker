from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, WebsiteActivitySerializer, SearchSerializer
from .models import Website_activity, Searches
from django.contrib.auth.models import User
from rest_framework.views import Response

class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Searches.objects.all()

class WebsiteActivityViewSet(viewsets.ModelViewSet):
    serializer_class = WebsiteActivitySerializer
    queryset = Website_activity.objects.all()
    