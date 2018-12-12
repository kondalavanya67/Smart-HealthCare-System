from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse

from .models import *
from .forms import enter_payment_details
from shopping_cart.views import get_user_pending_order
from .extras import generate_order_id

# Create your views here.


def payment_online_cod(request):
	customers = bank_customer.objects.all()
	admin_bank = get_object_or_404(bank_customer, customer_name='Admin')
	if request.method=="POST":
		form=enter_payment_details(request.POST or None)
		if form.is_valid():
			cus_name = form.cleaned_data['customer_name']
			bank_name = form.cleaned_data['Bank']
			Card_no = form.cleaned_data['card_no']
			ctype = form.cleaned_data['card_type']
			cvv_bc = form.cleaned_data['card_cvv']
			instance = bank_customer.objects.filter(Bank=bank_name, customer_name=cus_name, card_no=Card_no, card_type=ctype, card_cvv=cvv_bc).first()
			if instance:
				transId = generate_order_id()
				current_order = get_user_pending_order(request)
				new_payment = OnlinePayment.objects.create(transaction_id=transId,amount_paid=current_order.get_cart_total(),customer=instance)
				instance.bank_balance = instance.bank_balance - current_order.get_cart_total()
				admin_bank.bank_balance = admin_bank.bank_balance + current_order.get_cart_total()
				instance.save()
				admin_bank.save()
				current_order.is_ordered = True
				return redirect(reverse('shopping_cart:purchase_success', kwargs={'payment_mode':'Online-Payment'}))
	else:
		form = enter_payment_details()
	return render(request,'payment/payment_details.html',{'form': form,'customers' : customers,})
