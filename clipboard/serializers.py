from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Clipboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class ClipboardSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Clipboard
        fields = [ "user_id", "time", "text"]

class ClipboardGetSerializer(serializers.ModelSerializer):
    user = UsernameSerializer()
    
    class Meta:
        model = Clipboard
        fields = ["user", "time", "text"]