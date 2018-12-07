from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from .models import medicine
from django.http import HttpResponse

from .forms import *
from shopping_cart.models import Order, OrderItem
from rmp.models import rmpContact
# Create your views here.

@login_required(login_url='/rmp/login/')
def index(request):
	medicines = medicine.objects.all()
	if request.user:
		login_status = True
	else:
		login_status = False
	print(login_status)
	content = {
	"all_medicines" : medicines,
	"login_status"  : login_status,

	}
	return render(request, 'shoppingPortalApp/index_list.html',content)

def showMedicine_name(request, name):
    instance = get_object_or_404(medicine, name=name)
    user_profile = get_object_or_404(rmpContact, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    item_status = False
    if order:
    	order_temp = Order.objects.filter(owner=user_profile, is_ordered=False).first()
    	for item in order_temp.items.all():
    		if(instance.name==item.product.name):
    			item_status = True
    context_data = {
        "searched_medicine" : instance,
        "status" : item_status,
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
    form = add_medicine_Form(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.save()
        messages.success(request, "Succesfully Added")
    else:
    	messages.error(request, "Not Succesfully Added")
    context = {
        "form" : form,
        "page_name": "Add",
        "success" : "Succesfully Added",
        "failure" : "Not Succesfully Added"
    }
    return render(request,'shoppingPortalApp/index_add.html',context)

def added(request):
	context = {}
	return render(request,'shoppingPortalApp/added.html',context)


def index_delete(request):
	form = del_medicine_Form(request.POST or None)
	if form.is_valid():
		to_del = request.POST['name']	
		instance = get_object_or_404(medicine, name=to_del)
		instance.delete()
		messages.success(request, "Succesfully Deleted")
	else:
		messages.error(request, "No Such Medicine")
	context = {
        "form" : form,
    }
	return render(request, 'shoppingPortalApp/index_del.html',context)