from django import forms
from .models import Order, OrderItem


# class OrderItem_Quatity(forms.Form):
# 	QUANTITY_CHOICE = (
# 			(1,1),
# 			(2,2),
# 			(3,3),
# 			(4,4),
# 			(5,5),
# 		)
# 	quantity = models.IntegerField(choices = QUANTITY_CHOICE,initial=1)

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
	# class Meta:
	# 	model = Order
	# 	fields = [
	# 		'patient_phno',
	# 		'deliver_addr_houseno',
	# 		'deliver_addr_street',
	# 		'deliver_addr_pincode',
	# 		'deliver_addr_district',
	# 		'deliver_addr_state',
	# 		'deliver_addr_country',
	# 		'payment_method',
	# 	]