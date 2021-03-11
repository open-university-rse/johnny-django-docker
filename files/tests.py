from django.test import TestCase
from django.contrib.auth.models import User
from .models import Files
class FilesTest(TestCase):
    def test_user_details(self): 
        self.paul = User.objects.create_user(first_name="paul", last_name="lunn", username="user1", email="paul@email.com")       
        self.assertEqual(self.paul.username, "user1")
