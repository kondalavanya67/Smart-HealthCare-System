from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse

from .models import OrderItem, Order
from rmp.models import rmpContact
from shoppingPortalApp.models import medicine

from .forms import enter_paymentMethod
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
	order_item.quantity = 1
	user_order.items.add(order_item)
	if status:
		user_order.ref_code = generate_order_id()
		user_order.save()
	for item in user_order.items.all():
		item.quantity = 1
		item.save()
	# messages.info(request, "item added to cart")
	return redirect(reverse('shoppingPortalApp:medicine', kwargs={'name':product.name}))

def delete_from_cart(request, item_id):
	item_to_delete = OrderItem.objects.filter(pk=item_id)
	if item_to_delete.exists():
		item_to_delete[0].delete()
		# messages.info(request, "Item has been deleted from cart")	
	return redirect(reverse('shopping_cart:order_summary'))

def delete_from_cart2(request, item_id):
	item_to_delete = OrderItem.objects.filter(pk=item_id)
	print(item_to_delete)
	if item_to_delete.exists():
		item_to_delete[0].delete()
	return redirect(reverse('shoppingPortalApp:medicine', kwargs={'name':item_to_delete.order_item_name}))



def order_summary(request):
	existing_order = get_user_pending_order(request)
	context = {
		'order': existing_order,
	}
	return render(request, 'shopping_cart/order_summary.html', context)

def order_summary_ajax(request):
	existing_order = get_user_pending_order(request)
	quantity_dict = dict()
	for item in existing_order.items.all():
		quantity_no = request.GET.get(item.product.name)
		if quantity_no != None:
			print(int(quantity_no))
			item.quantity = int(quantity_no)
			item.save()
			quantity_dict[item.product.name] = item.quantity
	
	context = {'order': existing_order}
	return JsonResponse(quantity_dict)


def enter_address(request):
	existing_order = get_user_pending_order(request)
	user = request.user
	if request.method=="POST":
		form=enter_paymentMethod(request.POST)
		if form.is_valid():
			existing_order.patient_name = form.cleaned_data['patient_name']
			existing_order.patient_phno = form.cleaned_data['patient_phno']
			existing_order.deliver_addr_houseno = form.cleaned_data['deliver_addr_houseno']
			existing_order.deliver_addr_street = form.cleaned_data['deliver_addr_street']
			existing_order.deliver_addr_pincode = form.cleaned_data['deliver_addr_pincode']
			existing_order.deliver_addr_district = form.cleaned_data['deliver_addr_district']
			existing_order.deliver_addr_state = form.cleaned_data['deliver_addr_state']
			existing_order.deliver_addr_country = form.cleaned_data['deliver_addr_country']
			existing_order.payment_method = form.cleaned_data['payment_method']
			existing_order.save()
			if(existing_order.payment_method == "Cash On Delivery"):
				context = {

				}
				return redirect(reverse('shopping_cart:purchase_success_cod'))
			return redirect(reverse('shopping_cart:purchase_success'))
	else:

		form=enter_paymentMethod()
	return render(request,'shopping_cart/enter_address.html',{'form': form,})

def purchase_success(request):
	user_profile = get_object_or_404(rmpContact, user=request.user)
	current_order, status = Order.objects.get_or_create(owner=user_profile,is_ordered=False)
	current_order.is_ordered = True
	current_order.save()
	return render(request, 'shopping_cart/purchase_success.html', {})

def purchase_success_cod(request):
	user_profile = get_object_or_404(rmpContact, user=request.user)
	current_order, status = Order.objects.get_or_create(owner=user_profile,is_ordered=False)
	current_order.is_ordered = True
	context = {
		'p_name' : current_order.patient_name,
		'p_phno' : current_order.patient_phno,
		'p_houseno' : current_order.deliver_addr_houseno,
		'p_street' : current_order.deliver_addr_street,
		'p_district' : current_order.deliver_addr_district,
		'p_pincode' : current_order.deliver_addr_pincode,
		'p_state' : current_order.deliver_addr_state,
		'p_country' : current_order.deliver_addr_country,
	}
	current_order.save()
	return render(request, 'shopping_cart/purchase_success_cod.html',context)


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
