from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class login(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=20)

class register(models.Model):
	username = models.CharField(max_length=120)
	email=models.EmailField(max_length=120)
	password = models.CharField(max_length=20)
	password1 = models.CharField(max_length=20)
    