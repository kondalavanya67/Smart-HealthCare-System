from django.db import models
from django.urls import reverse
# Create your models here.
class Profile(models.Model):
#    doctor_id=models.CharField(max_length=200)
    Male = 'Male'
    Female = 'Female'

    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),

    )

    ORTHOPAEDIC='ORTHOPAEDIC'
    GYNACEOLOGIST= 'GYNACEOLOGIST'
    ONCOLOGIST='ONCOLOGIST'
    NEUROLOGIST='NEUROLOGIST'

    SPECIALITY_CHOICES=(
        (ORTHOPAEDIC, 'ORTHOPAEDIC'),
        (GYNACEOLOGIST, 'GYNACEOLOGIST'),
        (ONCOLOGIST,'ONCOLOGIST'),
        (NEUROLOGIST,'NEUROLOGIST'),



    )
    doctor_id=models.CharField(max_length=20,unique=True)
    profile_photo=models.ImageField(upload_to='media_/profile_pic/')
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=500)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    email_id=models.CharField(max_length=250)
    mobile_no=models.BigIntegerField()
    speciality=models.CharField(max_length=250, choices=SPECIALITY_CHOICES)
    qualification=models.CharField(max_length=250)
    locality=models.CharField(max_length=250)
    hospital=models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('doctor_profile:show_profile',kwargs={'pk':self.pk})
    def __str__(self):
        return self.first_name+' - '+ self.last_name
