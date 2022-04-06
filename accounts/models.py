from distutils.command.upload import upload
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class UserAvatar(models.Model):
  image = models.ImageField(upload_to='avatar', null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  
# class Profile(models.Model):
#   avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
  