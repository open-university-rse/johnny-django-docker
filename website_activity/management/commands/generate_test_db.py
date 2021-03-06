from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.apps import apps
from django.core import management
from datetime import datetime
from django.utils import timezone
import csv

# import models
from website_activity.models import Website_activity
from clipboard.models import Clipboard
from files.models import Files, createFileAndMetrics

MOCK_USER_FILE = "website_activity/management/commands/mock_users.csv"
MOCK_WEB_HISTORY_FILE = "website_activity/management/commands/mock_users.csv"
MOCK_IMAGE_FOLDER = "./media/"
# mock csv file columns = first_name,last_name,username,email,password,address,city,county,postal,phone1,phone2
MOCK_FIRST_NAME = 0
MOCK_LAST_NAME = 1
MOCK_USERNAME = 2
MOCK_EMAIL = 3
MOCK_PASSWORD = 4

NUM_MOCK_USERS = 3
history_json = {
    "username": "cbletsoe0",
    "history": [
        {
            "time": "1612536039.0",
            "url": "https://www.google.com/search?q=pytest+not+finding+tests"
        },
        {
            "time": "1612536201.0",
            "url": "https://docs.pytest.org/en/stable/example/pythoncollection.html#changing-naming-conventions"
        },
        {
            "time": "1612536854.0",
            "url": "https://www.google.com/search?q=+datetime.datetime"
        },
        {
            "time": "1612537811.0",
            "url": "https://www.google.com/search?ei=Pl0dYMnDA_LU1fAPxMuEoAg&q=datetime.datetime+unix+year&oq=datetime.datetime+unix+year&gs_lcp=CgZwc3ktYWIQAzIFCCEQoAE6BwgAEEcQsAM6AggAOgYIABAWEB46BwghEAoQoAE6BAghEBVQ5xpY7CRg8ypoAXACeACAAXaIAboDkgEDNS4xmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjJ2pCAgdPuAhVyahUIHcQlAYQQ4dUDCAw&uact=5"
        }
        
    ]
}

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # delete old
        management.call_command("delete_all")

        with open(MOCK_USER_FILE) as csvfile:
            mock_users = list(csv.reader(csvfile, delimiter=","))
            mock_index = 1

        #  lets create all the user profiles first
        for i in range(0, NUM_MOCK_USERS + 1):
            mock_details = mock_users[mock_index]
            new_user = User.objects.create_user(
                first_name=mock_details[MOCK_FIRST_NAME],
                last_name=mock_details[MOCK_LAST_NAME],
                username=mock_details[MOCK_USERNAME],
                email=mock_details[MOCK_EMAIL],
                password=mock_details[MOCK_PASSWORD],
            )
            mock_index += 1

        thisUser = User.objects.get(username="cbletsoe0")
        f_time = 1612537811.0
        dt = datetime.fromtimestamp(int(f_time))
        new_datetime = timezone.make_aware(dt, timezone.utc)
        
        time = datetime(2012, 1, 14, 12, 0, 0, tzinfo=timezone.utc)
        Website_activity.objects.create(user=thisUser, time=time, url="https://www.google.com/search?q=+datetime.datetime" )

        time = datetime(2012, 1, 14, 12, 1, 0, tzinfo=timezone.utc)
        Clipboard.objects.create(user= thisUser, time=time, text="owejcwoeifjcnwofej")

        time = datetime(2012, 1, 14, 12, 2, 0, tzinfo=timezone.utc)
        createFileAndMetrics(user=thisUser, time=time, text="print('hello world')", path = "home/paul/Desktop/intro.py")

        f = open("tests/advancedTest1.py", "r")
        advancedText = f.read()
        time = datetime(2012, 1, 14, 12, 2, 0, tzinfo=timezone.utc)
        createFileAndMetrics(user=thisUser, time=time, text=advancedText, path = "home/paul/Desktop/intro.py")

        thisUser2 = User.objects.get(username="gloynes1")
        f_time = 1612537600.0
        dt = datetime.fromtimestamp(int(f_time))
        new_datetime = timezone.make_aware(dt, timezone.utc)
        Website_activity.objects.create(user=thisUser2, time=new_datetime , url="https://www.google.com/search?q=Django+Debug+Toolbar" )

        Clipboard.objects.create(user= thisUser2, time=new_datetime, text="oiwejcunweoiucnwoeiuxdnwoeincwije")

        createFileAndMetrics(user= thisUser2, time=new_datetime, text="assert true", path = "home/paul/Desktop/math.py")

        # add me as a user
        paul = User.objects.create_user(
                first_name='Paul',
                last_name='Lunn',
                username='paulilunn',
                email='paul@johnny.co.uk',
                password="password",
            )

