from django.test import TestCase
from django.contrib.auth.models import User
from .models import Files, getBanditResult, getRadonResult, createFileAndMetrics, getProspectorResult
from django.utils import timezone
from freezegun import freeze_time
import datetime
from django.conf import settings
import json


class FilesTest(TestCase):
    def setUp(self):
        self.paul = User.objects.create_user(
            first_name="paul",
            last_name="lunn",
            username="user1",
            email="paul@email.com",
        )

    # @freeze_time("2012-01-14 12:00:01 UTC")
    # def testFileCreate(self):
    #     text = "this is the text"
    #     path = "/home/user/paul"
    #     newFile = Files.objects.create(user=self.paul, text=text, path=path)

    #     self.assertEqual(newFile.user, self.paul)
    #     self.assertEqual(newFile.text, text)
    #     self.assertEqual(newFile.path, path)
    #     self.assertEqual(
    #         newFile.time, datetime.datetime(2012, 1, 14, 12, 0, 1, tzinfo=timezone.utc)
    #     )

    def testTempFile(self):
        filename = settings.TEST_DIR + "python.py"
        f = open(filename, "w")
        f.write("hello django!")
        f.close()

        f = open(filename, "r")
        text = f.read()
        self.assertEqual(text, "hello django!")
        f.close()

    def testGetBanditFile(self):
        filename = settings.TEST_DIR + "testGetBanditFile.py"
        f = open(filename, "w")
        f.write("assert true")
        f.close()

        report = getBanditResult(filename)
        j = json.loads(report)
        self.assertEqual(j["results"][0]["test_id"], "B101")

    def testGetProspector(self):
        filename = settings.TEST_DIR + "testGetProspector.py"
        f = open(filename, "w")
        f.write("assert true")
        f.close()

        report = getProspectorResult(filename)
        j = json.loads(report)
        self.assertEqual(j["summary"]["libraries"], ['django'])

    def testGetRadonFile(self):
        # {"tests/temp/testGetRadonFile.py": {"loc": 1, "lloc": 1, "sloc": 1, "comments": 0, "multi": 0, "blank": 0, "single_comments": 0}}
        filename = settings.TEST_DIR + "testGetRadonFile.py"
        f = open(filename, "w")
        f.write("assert true")
        f.close()

        report = getRadonResult(filename)
        j = json.loads(report)
        self.assertEqual(j[filename]["loc"], 1)
        self.assertEqual(j[filename]["lloc"], 1)
        self.assertEqual(j[filename]["sloc"], 1)
        self.assertEqual(j[filename]["comments"], 0)
        self.assertEqual(j[filename]["multi"], 0)
        self.assertEqual(j[filename]["blank"], 0)
        self.assertEqual(j[filename]["single_comments"], 0)

    def testCreateFileAndMetrics(self):
        text = "assert true"
        path = "/home/user/paul"
        time = datetime.datetime(2012, 1, 14, 12, 0, 1, tzinfo=timezone.utc)

        newFile = createFileAndMetrics(user=self.paul, text=text, time=time, path=path)

        self.assertEqual(newFile.user, self.paul)
        self.assertEqual(newFile.text, text)
        self.assertEqual(newFile.path, path)
        self.assertEqual(
            newFile.time, datetime.datetime(2012, 1, 14, 12, 0, 1, tzinfo=timezone.utc)
        )

        self.assertEqual(newFile.loc, 1)
        self.assertEqual(newFile.lloc, 1)
        self.assertEqual(newFile.sloc, 1)
        self.assertEqual(newFile.comments, 0)
        self.assertEqual(newFile.multi, 0)
        self.assertEqual(newFile.blank, 0)
        self.assertEqual(newFile.singleComments, 0)

        self.assertEqual(newFile.banditIssues, '["B101"]')

        report = newFile.bandit
        j = json.loads(report)
        self.assertEqual(j["results"][0]["test_id"], "B101")

        pros = newFile.prospector
        j = json.loads(pros)
        self.assertEqual(j["summary"]["libraries"], ['django'])


    def testCreateFileAndMetrics2(self):
        text = "import pickle\nassert true\n"
        path = "/home/user/paul"
        time = datetime.datetime(2012, 1, 14, 12, 0, 1, tzinfo=timezone.utc)

        newFile = createFileAndMetrics(user=self.paul, text=text, time=time, path=path)

        self.assertEqual(newFile.user, self.paul)
        self.assertEqual(newFile.text, text)
        self.assertEqual(newFile.path, path)
        self.assertEqual(
            newFile.time, datetime.datetime(2012, 1, 14, 12, 0, 1, tzinfo=timezone.utc)
        )

        self.assertEqual(newFile.loc, 2)
        self.assertEqual(newFile.lloc, 2)
        self.assertEqual(newFile.sloc, 2)
        self.assertEqual(newFile.comments, 0)
        self.assertEqual(newFile.multi, 0)
        self.assertEqual(newFile.blank, 0)
        self.assertEqual(newFile.singleComments, 0)

        self.assertEqual(newFile.banditIssues, '["B403", "B101"]')

        report = newFile.bandit
        j = json.loads(report)
        self.assertEqual(j["results"][0]["test_id"], "B403")
        self.assertEqual(j["results"][1]["test_id"], "B101")

        pros = newFile.prospector
        j = json.loads(pros)
        self.assertEqual(j["summary"]["libraries"], ['django'])