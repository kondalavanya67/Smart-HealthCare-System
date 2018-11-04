from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from .models import medicine
from django.http import HttpResponse

from .forms import add_medicine_Form
# Create your views here.


def index(request):
	medicines = medicine.objects.all()
	content = {
	"page_name" : "Main",
	"all_medicines" : medicines,
	"key1" : 1,
	"key2" : 2,	
	}
	return render(request, 'shoppingPortalApp/index_list.html',content)

def showMedicine_name(request, name):
    instance = get_object_or_404(medicine, name=name)
    context_data = {
        "searched_medicine" : instance,
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
		"page_name" : "Search",
		"value" : False,
		"searchItem" : query
		}
	else:
		content = {
		"page_name" : "Search",
		"searched_medicine" : get_object_or_404(medicine, id=k),
		"value" : True,
		}
	return render(request, 'shoppingPortalApp/after_search.html',content)

def index_add(request):
    form = add_medicine_Form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.save()
        messages.success(request, "Succesfully Added")
    else:
    	messages.error(request, "Not Succesfully Added")
    context = {
        "form" : form,
        "page_name": "Add"
    }
    return render(request, 'shoppingPortalApp/index_add.html',context)

def index_delete(request, id=None):
	instance = get_object_or_404(medicine, id=id)
	instance.delete()
	messages.success(request, "Succesfully Deleted")
	return HttpResponse("Deleted")

"""def index_showMedicine(request, name):
	instance = get_object_or_404(medicine, name=name)
	context = {
		"instance" : instance,
		"page_name": "display"
	}
	return render(request,'shoppingPortalApp/index_showMedicine.html',context)"""