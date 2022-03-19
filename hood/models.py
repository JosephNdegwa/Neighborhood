from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)


class Neighbourhood(models.Model):
    neighbourhood_photo = models.ImageField(upload_to='neighbourhood/')
    neighbourhood_name = models.CharField(max_length=100, blank=True, null=True)
    occupants_count = models.IntegerField(blank=True, null=True)
    neighbourhood_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
