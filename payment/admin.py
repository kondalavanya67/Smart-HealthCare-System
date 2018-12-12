from django.contrib import admin

from .models import bank, OnlinePayment, bank_customer
# Register your models here.

admin.site.register(bank)
admin.site.register(OnlinePayment)
admin.site.register(bank_customer)
