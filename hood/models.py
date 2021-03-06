from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    occupants_count = models.IntegerField(blank=True, null=True)
    neighbourhood_location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=200)
    neighbourhood_location = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



class Business(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='owner')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='business')

    def __str__(self):
        return f'{self.name} business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()



class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    post = models.TextField()
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='poster')
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name='local_guy')



class NewMemberMail(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()



    
