from django.db import models
from django.contrib.auth.models import User
from doctor_profile.models import Profile
from rmp.models import rmpContact


class Post(models.Model):
    doctor_name = models.ForeignKey('doctor_profile.Profile', on_delete=models.CASCADE)


class Rmplist(models.Model):
    rmp_list = models.ForeignKey('rmp.rmpContact', on_delete=models.CASCADE)


class appointment(models.Model):
    patient_name = models.ForeignKey('booking.PaitentDetails', on_delete=models.CASCADE)
    booking = models.ForeignKey('booking.AppointmentDetials', on_delete=models.CASCADE)