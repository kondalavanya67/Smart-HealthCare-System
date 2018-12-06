from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def doctor_home_page(request):
	return render(request, "base.html")
