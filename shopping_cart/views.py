from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import OrderItem, Order
from rmp.models import rmpContact
from shoppingPortalApp.models import medicine

from .extras import generate_order_id
import random
# Create your views here.



def get_user_pending_order(request):
    user_profile = get_object_or_404(rmpContact, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0

def add_to_cart(request, item_id):

	user_profile = get_object_or_404(rmpContact, user=request.user)

	product = medicine.objects.filter(id=item_id).first()

	order_item, status = OrderItem.objects.get_or_create(product=product)
	user_order, status = Order.objects.get_or_create(owner=user_profile,is_ordered=False)
	user_order.items.add(order_item)
	if status:
		user_order.ref_code = generate_order_id()
		user_order.save()

	messages.info(request, "item added to cart")
	return redirect(reverse('shoppingPortalApp:medicine', kwargs={'name':product.name}))

def delete_from_cart(request, item_id):
	item_to_delete = OrderItem.objects.filter(pk=item_id)
	if item_to_delete.exists():
		item_to_delete[0].delete()
		messages.info(request, "Item has been deleted from cart")	
	return redirect(reverse('shopping_cart:order_summary'))

def delete_from_cart2(request, item_id):
	item_to_delete = OrderItem.objects.filter(pk=item_id)
	print(item_to_delete)
	if item_to_delete.exists():
		item_to_delete[0].delete()
	return redirect(reverse('shoppingPortalApp:medicine', kwargs={'name':item_to_delete.order_item_name}))



def order_summary(request):
	existing_order = get_user_pending_order(request)
	context = {'order': existing_order}
	return render(request, 'shopping_cart/order_summary.html', context)

def purchase_success(request):
	user_profile = get_object_or_404(rmpContact, user=request.user)
	current_order, status = Order.objects.get_or_create(owner=user_profile,is_ordered=False)
	current_order.is_ordered = True
	current_order.save()
	return render(request, 'shopping_cart/purchase_success.html', {})

def show_order_history(request):
    user_profile = get_object_or_404(rmpContact, user=request.user)
    order = Order.objects.filter(owner=user_profile,is_ordered=True)
    sum = 0
    for order_cost in order:
    	sum = sum + order_cost.get_cart_total()
    
    context = {
    	"orders" : order,
    	"order_count" : order.count(),
    	"total_order_count" : sum,
    	"user" : user_profile,
    	"check_orders" : Order.objects.all(),
    }
    return render(request, 'shopping_cart/order_history.html',context)