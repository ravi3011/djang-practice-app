from django.test import testcases
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new with an email is successful"""
        email = 'test@london.com'
        password = 'Test123'