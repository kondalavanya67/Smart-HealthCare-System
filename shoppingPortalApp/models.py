from django.db import models
from django.urls import reverse
# Create your models here.

class medicine(models.Model):
    name = models.CharField(max_length = 120)
    about = models.TextField()
    usage = models.TextField()
    manufacturedBy = models.CharField(max_length = 120)
    price = models.FloatField(null=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(null=True, blank=True)
    def get_absolute_url_page(self):
        return reverse("medicine",kwargs={"name": self.name})

    def __str__(self):
    	return self.name

		


