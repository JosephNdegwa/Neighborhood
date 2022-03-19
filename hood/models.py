from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)


class Neighborhood(models.Model):
    neighbourhood_name = models.CharField(max_length=100, blank=True, null=True)
    occupants_count = models.IntegerField(blank=True, null=True)
    neighbourhood_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Business(models.Model):
    business_name = models.CharField(max_length=100, blank=True, null=True)
    business_email = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    neighbourhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)


class User(models.Model):
    profile_photo = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=100, blank=True, null=True)
    status = models.TextField(max_length=140, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
