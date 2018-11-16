from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    doctor_id = models.CharField(max_length=100)
    doctor_name = models.ForeignKey(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
     return self.doctor_id

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})