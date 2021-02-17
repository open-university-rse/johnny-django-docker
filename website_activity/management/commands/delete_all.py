# command that can be called by manage.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from website_activity.models import Website_activity, Searches
from clipboard.models import Clipboard
from django.apps import apps


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # warning deletes all ********************************
        print("Deleting all database entries")
        try:
            User.objects.all().delete()
        except:
            pass
        try:
            Website_activity.objects.all().delete()
        except:
            pass
        try:
            Searches.objects.all().delete()
        except:
            pass
        try:
            Clipboard.objects.all().delete()
        except:
            pass
       
    