from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils.encoding import force_bytes, force_text
from .forms import  LoginForm, RegisterForm,Add_Rmp_Profile
from .models import rmpContact
from myapp.models import Rmplist,Profile
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.db import connection,IntegrityError
import random
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def login_page(request):
	form=LoginForm(request.POST or None)
	context= {
		"form":form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username6=form.cleaned_data.get("username6")
		password6=form.cleaned_data.get("password6")
		user=authenticate(request, username=username6, password=password6)
		if user is not None:

			print(user.is_authenticated)
			login(request, user)
			return redirect("/rmp/show_rmp_profile/")
		else:
			messages.error(request, 'Invalid login credentials')
			print("error")

	return render(request, "rmp/login.html", context=context)

#User = get_user_model()
#def register_page(request):
#	form=RegisterForm(request.POST or None)
#	context= {
#		"form":form
#	}
#
#	if form.is_valid():
#		print(form.cleaned_data)
#		username=form.cleaned_data.get("username")
#		email=form.cleaned_data.get("email")
#		password=form.cleaned_data.get("password")
#		new_user=User.objects.create_user(username=username, email=email, password=password)
#
#		login(request,new_user)
#		print(new_user)
#		return redirect('/rmp/make_rmp_profile/')
#
#	return render(request, "rmp/register.html", context=context)
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

            return render(request,'verify1.html', context)
    else:
    	form=RegisterForm()
    	messages.error(request, 'Invalid login credentials')
    context={
    'form':form
    }
    return render(request,'rmp/register.html',context)

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
			return redirect('/rmp/make_rmp_profile/')
	else:
		return HttpResponse('Please give correct OTP')
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
