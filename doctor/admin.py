from django.contrib import admin

# Register your models here.
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
	list_display=['__str__', 'slug']
	class Meta:
		model=Doctor


admin.site.register(Doctor, DoctorAdmin)