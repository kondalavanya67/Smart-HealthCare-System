from django.shortcuts import render

# Create your views here.
from .models import Cart


def cart_home(request):
	cart_obj, new_obj=Cart.objects.new_or_get(request)
	products=cart_obj.products.all()
	#print(Cart.objects.filter(products__is_null=True))
	total=0
	for x in products:
		total += x.price
	print(total)
	print(products)
	return render(request, "carts/home.html", {})
