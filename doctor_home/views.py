from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.
def doctor_home_page(request):
	return render(request, "base.html")