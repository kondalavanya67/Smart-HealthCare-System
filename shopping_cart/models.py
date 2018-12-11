from django.db import models
from django.core.validators import MinValueValidator

from rmp.models import rmpContact
from shoppingPortalApp.models import medicine
# Create your models here.

	# MEDICINE_TYPE_CHOICE = (
	# 		('syrup','syrup'),
	# 		('capsules','capsules'),
	# 	)
# medicine_type = models.CharField(max_length=20, choices = MEDICINE_TYPE_CHOICE)

class OrderItem(models.Model):
	product = models.OneToOneField(medicine,on_delete=models.CASCADE,primary_key=True,)
	is_ordered = models.BooleanField(default=False)
	quantity = models.IntegerField(default=1)
	date_added = models.DateTimeField(auto_now=True)
	date_ordered = models.DateTimeField(null=True)

	def __str__(self):
		return self.product.name

	def order_item_total(self):
		return self.quantity * self.product.price

	def order_item_name(self):
		return self.product.name

class Order(models.Model):
	PaymentMode = (
			('Cash On Delivery','Cash On Delivery'),
			('Pay Online','Pay Online'),
		) 
	ref_code = models.CharField(max_length=15)
	patient_name = models.CharField(max_length=15, null=True)
	patient_phno = models.IntegerField(null=True)
	is_ordered = models.BooleanField(default=False)
	items = models.ManyToManyField(OrderItem)
	date_added = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey(rmpContact, on_delete=models.SET_NULL, null=True)
	deliver_addr_houseno  = models.CharField(max_length=30, null=True)
	deliver_addr_street   = models.CharField(max_length=30, null=True)
	deliver_addr_pincode  = models.IntegerField(null=True)
	deliver_addr_district = models.CharField(max_length=20, null=True)
	deliver_addr_state    = models.CharField(max_length=15, null=True)
	deliver_addr_country  = models.CharField(max_length=15, null=True)
	payment_method = models.CharField(max_length=20, choices=PaymentMode)
	def get_cart_items(self):
	    return self.items.all()

	def get_no_of_cart_items(self):
		count = 0
		for item in self.items.all():
			count = count + 1
		return count

	def get_cart_total(self):
		return sum([item.product.price * item.quantity for item in self.items.all()])

	# def __str__(self):
	# 	return self.owner.first_name



