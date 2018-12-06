from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from rmp.models import rmpContact
import uuid
from uuid import uuid4
from doctor_profile.models import Profile,BookingDate,Slot
# Create your models here.

from uuid import uuid4

def generateUUID():
    return str(uuid4())

class PaitentDetails(models.Model):

    Male = 'Male'
    Female = 'Female'

    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),

    )


    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    doctor_id=models.ForeignKey(Profile,max_length=250, null=True,blank=True, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=500)
    age=models.IntegerField()
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_no=models.BigIntegerField()
    symptoms=models.CharField(max_length=250)
    description_of_illness=models.CharField(max_length=250)
    checkout_id = models.CharField(default=generateUUID, max_length=36, unique=True,editable=False)
    doctor_name=models.CharField(max_length=150)


    def __str__(self):
    	return str(self.id)

    def get_absolute_url_booking_confirmation(self):
        return reverse('booking:booking_confirmation',kwargs={'pk':self.pk})



class AppointmentDetials(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    viedo_chat_link=models.CharField(max_length=100)
    appointment_slot=models.CharField(max_length=150)
    doctor_id=models.ForeignKey(Profile,max_length=250, null=True,blank=True, on_delete=models.CASCADE)
    date=models.ForeignKey(BookingDate,max_length=250, null=True,blank=True, on_delete=models.CASCADE)
    time=models.ForeignKey(Slot,max_length=250,null=True,blank=True, on_delete=models.CASCADE)
    appointment_id=models.CharField(max_length=20)
    transaction_id=models.CharField(max_length=250)
    paitent=models.ForeignKey(PaitentDetails, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.pk)
