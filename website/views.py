from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from doctor_home.forms import LoginForm , RegisterForm

def home(request):
	context={
	   "premium_content":"Hello u r logged out"
	}
	if request.user.is_authenticated:
		context["premium_content"]="you are logged in"
	return render(request, "index.html", context=context)

def about(request):
	return render(request, "about.html", {})

def how_we_work(request):
	return render(request, "how_we_work.html", {})

def contact(request):
	return render(request, "contact.html", {})


def contact_page(request):
	contact_form=ContactForm(request.POST or None)
	context= {
	   "form":contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	return render(request, "contact.html", context=context)
def home_page(request):
    	return render(request, "base.html")
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
			return redirect("/login")
		else:
			print("error")

	return render(request, "login.html", context=context)

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
		return redirect('/profile/make_profile')

	return render(request, "register.html", context=context)
