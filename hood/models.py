from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)


class Neighborhood(models.Model):
    neighbourhood_name = models.CharField(max_length=100, blank=True, null=True)
    occupants_count = models.IntegerField(blank=True, null=True)
    neighbourhood_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Business(models.Model):
    business_name = models.CharField(max_length=100, blank=True, null=True)
    business_email = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

   #create_business()
    #delete_business()
    #find_business(business_id)
    #update_business()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=200)
    neighborhood_key = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.name


    
