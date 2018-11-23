from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse
from doctor_profile.models import Profile
from rmp.models import rmpContact


class Post(models.Model):
    doctor_name = models.ForeignKey('doctor_profile.Profile', on_delete=models.CASCADE)


class Rmplist(models.Model):
    rmp_list = models.ForeignKey('rmp.rmpContact', on_delete=models.CASCADE)
