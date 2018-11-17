from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from doctor_profile.models import Profile
from django.http import HttpResponse
from .forms import Add_PaitentDetails
from .models import PaitentDetails



def doctor_list(request):
	doctors = Profile.objects.all()
	context = {
	
	   "doctor" : doctors,
	}
	return render(request, 'booking/doctor_list.html',context=context)




def doctor_detail(request, pk):
    instance = get_object_or_404(Profile, pk=pk)
    context = {
        "doctor" : instance,
    }
    return render(request, 'booking/doctor_detail.html',context=context)

def enter_paitent_details(request, pk):
	user=request.user
	instance = get_object_or_404(Profile, pk=pk)
	if request.method=="POST":
		form=Add_PaitentDetails(request.POST, request.FILES ,initial={'user':user,'doctor_id':pk})
		if form.is_valid():
			paitent_details=form.save(commit=False)
			paitent_details.save()
			print(paitent_details)
			print(paitent_details.get_absolute_url_paitent)
			return redirect('view_paitent_details', pk=paitent_details.id)
	else:
		form=Add_PaitentDetails(initial={ 'user':user, 'doctor_id':pk})
	context = {
        "form":form
     }
	return render(request, 'booking/enter_paitent_details.html',context=context)
	


def view_paitent_details(request, pk):
	instance=get_object_or_404(PaitentDetails, pk=pk)
	context={
	    "paitent":instance
	}
	return render(request, 'booking/show_paitent_details.html',context=context)

    



