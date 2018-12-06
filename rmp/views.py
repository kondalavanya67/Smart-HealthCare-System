from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import  LoginForm, RegisterForm,Add_Rmp_Profile
from .models import rmpContact
from myapp.models import Rmplist,Profile
from shopping_cart.models import Order


def login_page(request):
	form=LoginForm(request.POST or None)
	context= {
		"form":form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user=authenticate(request, username=username, password=password)
		if user is not None:

			print(user.is_authenticated)
			login(request, user)
			return redirect("/rmp/show_rmp_profile/")
		else:
			print("error")

	return render(request, "rmp/login.html", context=context)

User = get_user_model()
def register_page(request):
	form=RegisterForm(request.POST or None)
	context= {
		"form":form
	}

	if form.is_valid():
		print(form.cleaned_data)
		username=form.cleaned_data.get("username")
		email=form.cleaned_data.get("email")
		password=form.cleaned_data.get("password")
		new_user=User.objects.create_user(username=username, email=email, password=password)

		login(request,new_user)
		print(new_user)
		return redirect('/rmp/make_rmp_profile/')

	return render(request, "rmp/register.html", context=context)

def make_profile(request):
	user = request.user
	if request.method=="POST":

		form=Add_Rmp_Profile(request.POST, request.FILES ,initial={'email_id':user.email})

		if form.is_valid():
			profile=form.save(commit=False)
			profile.user=user
			profile.save()
			new = rmpContact.objects.last()
			Rmplist.objects.create(rmp_list=new)
		return redirect('/rmp/show_rmp_profile/')
	else:
		form=Add_Rmp_Profile(initial={'user':user,'email_id':user.email})
		return render(request,'rmp/make_rmp_profile.html',{'form':form})

def modify_profile(request):
	user = request.user
	profile = Profile.objects.get(user=user)
	form=Add_Rmp_Profile(request.POST or None, instance=profile)
	if form.is_valid():
		form.save()
		return redirect('/show_rmp_profile/')
	return render(request,'rmp/make_rmp_profile.html',{'form':form})

def Show_Profile(request):
	user = request.user
	profile = rmpContact.objects.get(user=user)
	context={
		'profile':profile
	}
	return render(request,'rmp/show_rmp_profile.html',context)

def myOrders(request):
	user = request.user
	my_user_profile = rmpContact.objects.get(user=user)
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders' : my_orders,
	}
	return render(request,'rmp/show_rmp_profile.html',context)

