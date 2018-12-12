from django import forms
from .models import Order, OrderItem



class enter_paymentMethod(forms.Form):
	PaymentMode = (
			('Cash On Delivery','Cash On Delivery'),
			('Pay Online','Pay Online'),
		) 

	patient_name = forms.CharField(max_length=15)
	patient_phno = forms.IntegerField()
	deliver_addr_houseno  = forms.CharField(max_length=30)
	deliver_addr_street   = forms.CharField(max_length=30)
	deliver_addr_pincode  = forms.IntegerField()
	deliver_addr_district = forms.CharField(max_length=20)
	deliver_addr_state    = forms.CharField(max_length=15)
	deliver_addr_country  = forms.CharField(max_length=15)
	payment_method = forms.ChoiceField(choices=PaymentMode)