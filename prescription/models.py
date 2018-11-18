from django.db import models
from django.urls import reverse
from doctor_profile.models import Profile
# Create your models here.
from django.urls import reverse
from doctor_profile.models import Profile

class Prescription(models.Model):
    #doctor_id=models.CharField(max_length=200)
    doctor=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    prescription_id=models.CharField(max_length=30,unique=True)
    prescription_date=models.DateTimeField(auto_now_add=True)
    pdf= models.FileField(upload_to='media_/pdf/', null=True, blank=True)
    #doctor_id=models.ForeignKey(Profile,)
    #doctor_name=models.CharField(max_length=30)
    #patient_name=models.CharField(max_length=30)
    def __str__(self):
        return self.prescription_id

    def get_absolute_url(self):
        return reverse('prescription:detail',kwargs={'pk':self.pk})



class Item(models.Model):
    prescription=models.ForeignKey(Prescription,on_delete=models.CASCADE)
    medicine_name=models.CharField(max_length=100,blank=False)
    days=models.BigIntegerField()
    morning=models.BooleanField(default=True)
    afternoon=models.BooleanField(default=True)
    night=models.BooleanField(default=True)



    def __str__(self):
        return self.medicine_name

class Medicine(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(name__lte=self.name)
