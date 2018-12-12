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
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.urls import reverse_lazy
from myapp.forms import contactForm,newsLetter
from django import forms


def home(request):
	if request.method == "POST":
		form=newsLetter(request.POST, request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()
			print(instance)
			return redirect('home')
	else:
		form = newsLetter()
	context ={
	    "form":form,
	}
	return render(request, "index.html", context=context)

@login_required(login_url=reverse_lazy('login'))
def doctor_home(request):
	user = request.user
	profile = Profile.objects.get(user=user)

	context={

		"premium_content":"Hello u r logged out",
		"profile":profile
	}
	if request.user.is_authenticated:
		context["premium_content"]="you are logged in"
	if(profile.verified==True):
		print('&&')
		return render(request,'doctor_homepage.html',context)
	else:
		print('%%')
		return redirect(reverse('doctor_profile:verification'))

	# return render(request, "doctor_homepage.html", context=context)


def about(request):
	return render(request, "about.html", {})

def how_we_work(request):
	return render(request, "how_we_work.html", {})


def contact(request):
	if request.method=="POST":
		form=contactForm(request.POST, request.FILES)
		if form.is_valid():
			details=form.save(commit=False)
			details.save()
			print(details)

			return redirect('contact')
	else:
		form  = contactForm()
	context = {
        "form":form,
     }
	return render(request, 'contact.html',context=context)

def contact_page(request):

    return render(request, "contact_page.html", {'first_name':first_name,'last_name':last_name,'email':email,'mobile_no':mobile_no,'message':message})



def doctor_contact(request):
	return render(request, "contact_doctor.html", {})

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
			messages.error(request, 'Invalid login credentials')
			print("error")

	return render(request, "login.html", context=context)

def email_verify(form):
	rand_numb=random.randint(10000, 999999)
	global b
	b=str(rand_numb)
	email=[form.data['email']]
	response=send_mail("OTP for email activation",b,"smarthealthcaresystemiiits@gmail.com",email)
	return b

#User = get_user_model()
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            b=email_verify(form)
            print(b)
            username=form.data['username']
            email=form.data['email']
            password1=form.data['password']
            context={
            'username':username,
            'email':email,
            'password':password1,
            'b':b,
            }

            return render(request,'verify.html', context)
    else:
    	form=RegisterForm()
    	messages.error(request, 'Invalid login credentials')
    context={
    'form':form
    }
    return render(request,'register.html',context)

#User = get_user_model()
def new_user_reg(request):
	if b == request.POST['token']:
		if request.method =='POST':
			username=request.POST.get('username',False)
			email=request.POST.get('email',False)
			password=request.POST.get('password',False)
			new_user=User.objects.create(username=username,email=email)
			new_user.set_password(request.POST['password'])
			new_user.save()
			login(request,new_user)
			print(new_user)
			return redirect('/profile/make_profile')
	else:
		return HttpResponse('Please give correct OTP')


def reset_password(request):
	if request.method=='POST':
		form=ResetForm(request.POST)
		if form.is_valid():
			mail=form.cleaned_data.get('email')
			global otp2
			for i in range(6):
				otp2=otp2_str(random.randint(0,9))
			mail_subject='otp verification to reset yoour password'
			message='your otp is' + otp2
			send_mail(
				mail_subject,
				message,
				'smarthealthcaresystemiiits@gmail.com'
				[mail],

				)
			request.session['email']=mail
			return render(request, 'otp2.html')
		else:
			return HttpResponse('Please give correct email')
	else:
		form1=ResetForm()
		return render(request, 'reset_email.html' , {'form':form1})



def log_out(request):
	logout(request)

	return redirect('/')
