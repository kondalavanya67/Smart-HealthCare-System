from django.contrib import admin
from .models import Profile,BookingDate,Slot
# Register your models here.
admin.site.register(Profile)
admin.site.register(BookingDate)
admin.site.register(Slot)
