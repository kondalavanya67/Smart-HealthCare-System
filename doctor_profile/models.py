from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime
from django.db.models.signals import pre_save
#from booking.models import AppointmentDetials

# Create your models here.
class Profile(models.Model):

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

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    profile_photo=models.ImageField(upload_to='media_/profile_pic/')
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=500)
    dob= models.DateField(default=date.today )
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    email_id=models.CharField(max_length=250)
    mobile_no=models.BigIntegerField()
    speciality=models.CharField(max_length=250, choices=SPECIALITY_CHOICES)
    qualification=models.CharField(max_length=250)
    locality=models.CharField(max_length=250)
    hospital=models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('booking:doctor_detail',kwargs={'pk':self.pk})

    def get_absolute_url_show(self):
        return reverse('myapp:doctor_detail',kwargs={'pk':self.pk})

    def get_absolute_url_upcoming_appointments(self):
        return reverse('myapp:doctor_upcoming_appointments',kwargs={'pk':self.pk})
    def get_absolute_url_attended_appointments(self):
        return reverse('myapp:doctor_attended_appointments',kwargs={'pk':self.pk})
    def get_absolute_url_slot(self):
        return reverse('myapp:doctor_slot',kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.id)

    def get_absolute_url_booking(self):
        return reverse('booking:enter_paitent_details',kwargs={'pk':self.pk})

# def profile_pre_save_reciever(sender,instance,*args,**kwargs):
#     if len(instance.mobile_no) != 10:
#         raise


class BookingDate(models.Model):
    doctor=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True,blank=True)
    date=models.DateField(default=datetime.now)

    def __str__(self):
        return str(self.date)
    def get_absolute_url(self):
        return reverse('doctor_profile:create_slot',kwargs={'pk':self.pk})

class Slot(models.Model):
    TIME_CHOICES = (('09:00:00', '9 am'),
                    ('12:00:00', '12 pm'),
                    ('16:00:00', '4 pm'), )
    doctor=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True,blank=True)
    date=models.ForeignKey(BookingDate,on_delete=models.CASCADE, null=True,blank=True)
    start_time=models.CharField(max_length=200,choices=TIME_CHOICES,null=True,blank=True)
    slot_status=models.BooleanField(default=False)

    class Meta:
        unique_together = ('doctor','start_time','date')



    def __str__(self):
    	return str(self.start_time)
