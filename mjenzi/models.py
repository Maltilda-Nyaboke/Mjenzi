from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    name = models.CharField(max_length=75, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='images')
    contact = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


    def save_profile(self):
        self.save()   

    def delete_profile(self):
        self.delete()
        
    @classmethod
    def search_profiles(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term).all()
        return profiles

    def __str__(self):
        return self.bio


