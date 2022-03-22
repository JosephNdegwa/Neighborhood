from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Profile, Business, Neighborhood

class ProfileTestCase(TestCase):
    def setUp(self):
        self.profile = User.objects.create(username="ken")
    
    def test_proxy_user(self):
        self.profile.bio = ""
        self.assertEqual(self.profile.bio, "")

class BusinessTestCase(TestCase):
    def setUp(self):
        self.owner = User.objects.create(username="joseph")
        self.business = Business.objects.create(owner=self.owner, business=self.business)

    def test_follow(self):
        self.assertEqual(self.business.owner, self.owner)
        self.assertEqual(self.business.business, self.business)


