from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Files

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class FilesPostSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Files
        fields = ["user_id", "time", "text", "path"]

class FilesGetSerializer(serializers.ModelSerializer):
    user = UsernameSerializer()
    
    class Meta:
        model = Files
        fields = ["user", "time", "text", "path"]