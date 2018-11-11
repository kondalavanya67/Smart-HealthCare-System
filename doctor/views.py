from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from .models import Doctor

# Create your views here.

class DoctorListView(ListView):
	queryset=Doctor.objects.all()


def doctor_list_view(request):
	print(request.session.get("first_name"))
	queryset=Doctor.objects.all()
	context={
	   'object_list':queryset
	}
	return render(request, "doctor/list_view.html", context=context)

def doctor_detail_view(request, pk=None):
	instance=get_object_or_404(Doctor, pk=pk)
	context={
	    'object':instance
	}
	return render(request, "doctor/detail_view.html", context=context)