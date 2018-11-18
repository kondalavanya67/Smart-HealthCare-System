from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from doctor_profile.models import Profile
from django.http import HttpResponse
from .forms import *
from .models import PaitentDetails,AppointmentDetials
import random
from django.db.models import Max


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
			#request.session['patient_id']=paitent_details.pk
			paitent_details.save()
			print(paitent_details)

			return redirect('booking:view_paitent_details', pk=paitent_details.id)
	else:
		form  = Add_PaitentDetails(initial={ 'user':user, 'doctor_id':pk})
		#form1 = Add_PatientToAppointment(initial={'patient':form})
	context = {
        "form":form,
     }
	return render(request, 'booking/enter_paitent_details.html',context=context)



def view_paitent_details(request, pk):
	instance=get_object_or_404(PaitentDetails, pk=pk)
	context={
	    "paitent":instance
	}
	return render(request, 'booking/show_paitent_details.html',context=context)

def booking_confirmation(request, pk):
	print("**")
	string= random.randint(100000000,10000000000000)
	viedo_chat_link="https://appr.tc/r/"+str(string)
	max_id=AppointmentDetials.objects.all().aggregate(Max('appointment_id'))
	if list(max_id.values())[0] == None:
		value=0
	else:
		value=int(list(max_id.values())[0])
	appointment_id=value+1

	max_id=AppointmentDetials.objects.all().aggregate(Max('transaction_id'))
	if list(max_id.values())[0] == None:
		value=100000
	else:
		value=int(list(max_id.values())[0])
	transaction_id=value+1
	instance=get_object_or_404(PaitentDetails,pk=pk)
	doctor_id=instance.doctor_id
	#patient_id=request.session['patient_id']
	#patient_obj=get_object_or_404(PaitentDetails,pk=patient_id)
	obj=AppointmentDetials.objects.create(viedo_chat_link=viedo_chat_link,transaction_id=transaction_id,appointment_id=appointment_id,doctor_id=doctor_id,paitent=instance)
	obj.save()

	context={
	   "paitent":instance,
	    "object":obj,
	}
	return render(request,'booking/booking_confirmation.html', context=context)
