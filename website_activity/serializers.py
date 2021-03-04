from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Website_activity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class WebsiteActivitySerializer(serializers.ModelSerializer):
    # user = UsernameSerializer()
    user_id = serializers.IntegerField()
    class Meta:
        model = Website_activity
        fields = ["user_id", "time", "url", "title"]

class WebsiteActivityGetSerializer(serializers.ModelSerializer):
    user = UsernameSerializer()
    
    class Meta:
        model = Website_activity
        fields = ["user", "time", "url", "title"]