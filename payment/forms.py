from django import forms
from .models import *


class enter_payment_details(forms.ModelForm):
	class Meta:
		model = bank_customer
		fields = '__all__'
		exclude = ('bank_balance',)