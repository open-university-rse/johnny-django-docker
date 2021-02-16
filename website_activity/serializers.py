from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Website_activity, Searches

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class SearchSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Searches
        fields = ["user", "time", "text"]

class WebsiteActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Website_activity
        fields = ["user", "time", "url"]