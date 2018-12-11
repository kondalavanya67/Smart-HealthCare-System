from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from .models import medicine
from django.http import HttpResponse
from django.urls import reverse,reverse_lazy
from .forms import *
from shopping_cart.models import Order, OrderItem
from rmp.models import rmpContact
# Create your views here.


def get_user_pending_order(request):
    user_profile = get_object_or_404(rmpContact, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


@login_required(login_url=reverse_lazy('rmp:login_rmp_profile'))
def index(request):
	medicines = medicine.objects.all()
	existing_order = get_user_pending_order(request)
	if request.user:
		login_status = True
	else:
		login_status = False
	print(login_status)
	content = {
	"all_medicines" : medicines,
	"login_status"  : login_status,
	"current_order" : existing_order,
	}
	return render(request, 'shoppingPortalApp/index_list.html',content)

def showMedicine_name(request, name):
    instance = get_object_or_404(medicine, name=name)
    user_profile = get_object_or_404(rmpContact, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    item_status = False
    existing_order = get_user_pending_order(request)
    if order:
    	order_temp = Order.objects.filter(owner=user_profile, is_ordered=False).first()
    	for item in order_temp.items.all():
    		if(instance.name==item.product.name):
    			item_status = True
    print()
    context_data = {
        "searched_medicine" : instance,
        "status" : item_status,
        'current_order':existing_order,
    }
    return render(request, 'shoppingPortalApp/result.html',context_data)




def result(request):
	medicines = medicine.objects.all()
	query = request.GET['query']
	temp = query.upper()
	k = 0
	for search_medicine in medicines:
		if search_medicine.name.upper() == temp:
			k = search_medicine.id
	if(k == 0):
		content = {
		"all_medicines" : medicines,
		"value" : False,
		"searchItem" : query
		}
	else:
		content = {
		"all_medicines" : medicines,
		"searched_medicine" : get_object_or_404(medicine, id=k),
		"value" : True,
		}
	return render(request, 'shoppingPortalApp/after_search.html',content)

def index_add(request):
	if request.method=="POST":
		form = add_medicine_Form(request.POST or None,request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect(reverse('shoppingPortalApp:successful_add',kwargs={'name':"added",}))
			# messages.success(request, "Succesfully Added")
	else:
		form = add_medicine_Form(request.POST or None,request.FILES or None)
	context = {
	"form" : form,
	}
	return render(request,'shoppingPortalApp/index_add.html',context)

    

def added(request,name):
	context = {'action':name,}
	return render(request,'shoppingPortalApp/added.html',context)


def index_delete_edit(request):
	form = del_medicine_Form(request.POST or None)
	medicines = medicine.objects.all()
	to_del = None
	print("hellohello")
	if request.method == 'POST':
		if form.is_valid():
			to_del = form.cleaned_data['name_to_del']
	if to_del:
		medicines = medicine.objects.filter(name=to_del)
	else:
		medicines = medicine.objects.all()
	context = {
        "form" : form,
        "medicines" : medicines,
    }
	return render(request, 'shoppingPortalApp/index_del.html',context)


def delete(request,med_id):
	instance = get_object_or_404(medicine,id=med_id)
	instance.delete()
	return redirect(reverse('shoppingPortalApp:del_edit_medicine'))

def update_medicine(request,med_id):
    instance = medicine.objects.get(id=med_id)
    form=Modify_Medicine_Form(request.POST or None, instance=instance)
    if form.is_valid():
            form.save()
            return redirect(reverse('shoppingPortalApp:successful_add', kwargs={'name':"edited",}))
    return render(request,'shoppingPortalApp/update_medicine.html',{'form':form})