from django.db import models

from rmp.models import rmpContact
from shoppingPortalApp.models import medicine
# Create your models here.


class OrderItem(models.Model):
	product = models.OneToOneField(medicine,on_delete=models.CASCADE,primary_key=True,)
	is_ordered = models.BooleanField(default=False)
	date_added = models.DateTimeField(auto_now=True)
	date_ordered = models.DateTimeField(null=True)

	def __str__(self):
		return self.product.name

	def order_item_name(self):
		return self.product.name

class Order(models.Model):
	ref_code = models.CharField(max_length=15)
	# patient_name = models.CharField(max_length=15)
	is_ordered = models.BooleanField(default=False)
	items = models.ManyToManyField(OrderItem)
	date_added = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey(rmpContact, on_delete=models.SET_NULL, null=True)

	def get_cart_items(self):
	    return self.items.all()

	def get_cart_total(self):
		return sum([item.product.price for item in self.items.all()])

	def __str__(self):
		return self.owner.first_name



