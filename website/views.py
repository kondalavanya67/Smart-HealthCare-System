from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model, logout
from doctor_home.forms import LoginForm , RegisterForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.db import connection,IntegrityError
import random
from django.contrib.auth.models import User
from doctor_profile.views import Profile
def home(request):
	context={
	   "premium_content":"Hello u r logged out"
	}
	if request.user.is_authenticated:
		context["premium_content"]="you are logged in"
	return render(request, "index.html", context=context)

def doctor_home(request):
	user = request.user
	profile = Profile.objects.get(user=user)

	context={

	   "premium_content":"Hello u r logged out",
	   "profile":profile
	}
	if request.user.is_authenticated:
		context["premium_content"]="you are logged in"
	return render(request, "doctor_homepage.html", context=context)


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
			return redirect("/doctor_home")
		else:
			print("error")

	return render(request, "login.html", context=context)

def email_verify(form):
	rand_numb=random.randint(10000, 999999)
	b=str(rand_numb)
	email=[form.data['email']]
	response=send_mail("hi",b,"smarthealthcaresystemiiits@gmail.com",email)
	return b

#User = get_user_model()
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            b=email_verify(form)
            print(b)
            username=form.data['username']
            email=form.data['email']
            password1=form.data['password1']
            context={
            'username':username,
            'email':email,
            'password1':password1,
            'b':b,
            }

            return render(request,'verify.html', context)
    else:
    	form=RegisterForm()
    context={
    'form':form
    }
    return render(request,'register.html',context)

#User = get_user_model()
def new_user_reg(request):
	if request.method =='POST':
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		new_user=User.objects.create(username=username,email=email)
		new_user.set_password(request.POST['password'])
		new_user.save()
		login(request,new_user)
		print(new_user)
		return redirect('/profile/make_profile')


def log_out(request):
	logout(request)
	return redirect('/')
