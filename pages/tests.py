from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class PagesTest(TestCase):
    def setUp(self):
        self.testUser = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123"
        )
        
    
    def test_user_exist(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(user.username, self.testUser.username)
    def test_template_(self):
        user = get_user_model().objects.get(id=1)
        
        self.assertEqual(user.username, self.testUser.username)
        self.assertFalse(user.is_superuser)
        