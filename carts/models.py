from django.db import models
from django.conf import settings
from doctor.models import Doctor
from django.db.models.signals import pre_save, post_save

# Create your models here.
User=settings.AUTH_USER_MODEL
# Create your models here.

class CartManager(models.Manager):
	def new_or_get(self, request):
		cart_id=request.session.get("cart_id", None)
		qs=self.get_queryset().filter(id=cart_id)
		if qs.count()==1:
			new_obj=False
			cart_obj=qs.first()
			print(cart_id)
			if request.user.is_authenticated and cart_obj.user is None:
				cart_obj.user=request.user
				cart_obj.save()
		else:
			cart_obj=Cart.objects.new(user=request.user)
			new_obj=True
			request.session["cart_id"]=cart_obj.id
		return cart_obj, new_obj

	def new(self, user=None):
		user_obj=None
		if user is not None:
			if user.is_authenticated:
				user_obj=user
		return self.model.objects.create(user=user_obj)


class Cart(models.Model):
	user=models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
	products=models.ManyToManyField(Doctor, blank=True)
	total=models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	updated=models.DateTimeField(auto_now=True)
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)

	objects = CartManager()

def pre_save_cart_receiver(sender, instance, *args, **kwargs):
	total=0
	products=instance.products.all()
	for x in products:
		total += x.price
	print(total)
	instance.total=total


pre_save.connect(pre_save_cart_receiver,sender=Cart)


