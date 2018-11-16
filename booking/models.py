from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from rmp.models import rmpContact
# Create your models here.


class PaitentDetails(models.Model):
    
    Male = 'Male'
    Female = 'Female'

    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),

    )

 
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=500)
    age=models.IntegerField()
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_no=models.BigIntegerField()
    symptoms=models.CharField(max_length=250)
    description_of_illness=models.CharField(max_length=250)

    def __str__(self):
    	return str(self.id)


class AppointmentDetials(models.Model):
	paitent_id=models.ForeignKey(PaitentDetails, on_delete=models.CASCADE)
	appointment_id=models.CharField(max_length=20)
	doctor_id=models.CharField(max_length=250)
	rmp_id=models.CharField(max_length=250)
	transaction_id=models.CharField(max_length=250)









    
    

        
   
        





    
    

    