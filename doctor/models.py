from django.db import models
import os
import random
from django.db import models

def get_filename_ext(filepath):
	base_name=os.path.basename(filepath)
	name,ext=os.path.splitext(base_name)
	return name,ext

def upload_image_path(instance, filename):
	new_filename=random.randint(1,50000)
	name,ext=get_filename_ext(filename)
	final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "doctor/{new_filename}/{final_filename}".format(
		             new_filename=new_filename,final_filename=final_filename)


# Create your models here.
class Doctor(models.Model):
	username=models.CharField(max_length=20)
	slug=models.SlugField(default="abc")
	description=models.TextField()
	price=models.DecimalField(decimal_places=2,max_digits=10, default=40.5)
	image=models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	active=models.BooleanField(default=False)

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return "/doctor/doctor_detail/{id}/".format(id=self.id)
    