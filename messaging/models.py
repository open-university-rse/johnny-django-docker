from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

MESSAGE_TYPE_DEBUG = 0
MESSAGE_TYPE_TWITTER = 1
MESSAGE_TYPE_SLACK = 2
MESSAGE_TYPE_EMAIL = 3
MESSAGE_TYPE_IDE = 4

# Create your models here.
class Messaging(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    text = models.TextField(blank=True)
    messageType = models.TextField(blank=True)

    def sendMessage(self, user, text, messageType):
        # add to database
        Messaging.objects.create(user=user, text=text, messageType=messageType)

        # send messages
        if messageType == MESSAGE_TYPE_DEBUG:
            print(f"DEBUG MESSAGE for {user.username} - text = {text}")
        if messageType == MESSAGE_TYPE_IDE:
            pass
        elif messageType == MESSAGE_TYPE_TWITTER:
            pass
        elif messageType == MESSAGE_TYPE_SLACK:
            pass
        elif messageType == MESSAGE_TYPE_EMAIL:
            pass



