from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


GENDER_CHOICES = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('others','OTHERS'),
)
class rmpLogData(models.Model):
	userlogId=models.CharField(primary_key=True, max_length=20)
	email=models.CharField(max_length=120)
	password = models.CharField(max_length=50)
	
class rmpContactDetail(models.Model):
	userlogId=models.ForeignKey(rmpLogData, on_delete=models.CASCADE, null=True)
	fullname=models.CharField(max_length=120)
	age=models.IntegerField( default=25,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
	gender=models.CharField(max_length=10,choices=GENDER_CHOICES, default='male')
	qualifications=models.CharField(max_length=30)
	locality=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	district=models.CharField(max_length=100)
	country=models.CharField(max_length=100)
	pin_code=models.CharField(max_length=6)
	phone_no=models.CharField(max_length=11)
	

		
class rmpPatientDetails(models.Model):
	rmp_id=models.ForeignKey(rmpLogData,on_delete=models.CASCADE,null=True)
	paitent_id=models.CharField(unique=True, max_length=10, null=True)
	paitent_fullname=models.CharField(max_length=120)
	paitent_age=models.IntegerField( default=25,validators=[MaxValueValidator(100), MinValueValidator(1)])
	paitent_gender=models.CharField(max_length=10,choices=GENDER_CHOICES, default='male')
	paitent_locality=models.CharField(max_length=100)
	paitent_city=models.CharField(max_length=100)
	paitent_district=models.CharField(max_length=100)
	paitent_country=models.CharField(max_length=100)
	paitent_type_of_ailment=models.CharField(max_length=120)
	description_of_ailment=models.CharField(max_length=120)
	paitent_phone_no=models.CharField(max_length=11)
	
	

	