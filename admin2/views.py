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
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def admin_home(request):
	return render(request, 'admin2/index.html')
