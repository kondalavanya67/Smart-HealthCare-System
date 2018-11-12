from django.contrib import admin
from .models import Prescription
from .models import Medicine
# Register your models here.
admin.site.register(Prescription)
admin.site.register(Medicine)
