from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from shoppingPortalApp.models import medicine
# Create your models here.


class rmpContact(models.Model):
    
    Male = 'Male'
    Female = 'Female'

    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),

    )

   
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    profile_photo=models.ImageField(upload_to='media_/profile_pic/')
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=500)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    email_id=models.CharField(max_length=250)
    mobile_no=models.BigIntegerField()
    qualification=models.CharField(max_length=250)
    locality=models.CharField(max_length=250)
    hospital=models.CharField(max_length=250)

    medicines = models.ManyToManyField(medicine, blank=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('myapp:myapp-fullrmplist',kwargs={'pk':self.pk})

    def get_absolute_url_rmp_upcoming_appointments(self):
        return reverse('myapp:rmp_upcoming_appointments', kwargs={'pk': self.pk})
    def get_absolute_url_rmp_attended_appointments(self):
        return reverse('myapp:rmp_attended_appointments', kwargs={'pk': self.pk})

    def get_absolute_url_rmp_patientdetail(self):
        return reverse('myapp:myapp-patientdetail', kwargs={'pk': self.pk})