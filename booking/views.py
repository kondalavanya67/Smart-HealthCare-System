from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from doctor_profile.models import Profile,BookingDate
from django.http import HttpResponse
from .forms import *
from .models import PaitentDetails,AppointmentDetials
import random
from django.db.models import Max
from django.views.generic import FormView, CreateView
from doctor_profile.models import BookingDate,Slot
from django.contrib.auth.decorators import login_required

@login_required(login_url=('rmp:login_rmp_profile'))
def doctor_list(request):
	doctors = Profile.objects.all()
	context = {

	   "doctor" : doctors,
	}
	return render(request, 'booking/doctor_list.html',context=context)



@login_required(login_url=('rmp:login_rmp_profile'))
def doctor_detail(request, pk):
    instance = get_object_or_404(Profile, pk=pk)
    context = {
        "doctor" : instance,
    }
    return render(request, 'booking/doctor_detail.html',context=context)

@login_required(login_url=('rmp:login_rmp_profile'))
def search_doctor(request):
	search = request.GET['searching_doctor']
	temp = search.upper()
	doctors = Profile.objects.all()
	k_name = 404
	k_speciality = 404
	for doctor in doctors:
		if doctor.first_name.upper() == temp:
			k_name = doctor.id
	if(k_name==404):
		for doctor in doctors:
			if doctor.last_name.upper() == temp:
				k_name = doctor.id
	speciality_doctors = Profile.objects.filter(speciality=temp)
	if(speciality_doctors.count()):
		k_speciality = 1
	if(k_name==404):
		if(k_speciality==1):
			context = {
			"key" : False,
			"key1": True,
			"speciality_doctors":speciality_doctors,
			}
		else:
			context = {
			"key" : False,
			"query":search,
			"key1" : False,
			}
	else:
		if(k_speciality==1):
			context = {
			"key" : True,
			"searched_doctor" : get_object_or_404(Profile,id=k_name),
			"key1": True,
			"speciality_doctors":speciality_doctors,
			}
		else:
			context = {
			"key" : True,
			"searched_doctor" : get_object_or_404(Profile,id=k_name),
			"key1" : False,
			}
	print()
	print(context)
	print()
	return render(request, 'booking/search.html',context)

@login_required(login_url=('rmp:login_rmp_profile'))
def enter_paitent_details(request, pk):
	user=request.user
	instance = get_object_or_404(Profile, pk=pk)

	if request.method=="POST":
		form=Add_PaitentDetails(request.POST, request.FILES)
		if form.is_valid():


			paitent_details=form.save(commit=False)
			#request.session['patient_id']=paitent_details.pk
			paitent_details.user=user
			paitent_details.doctor_id=instance
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


@login_required(login_url=('rmp:login_rmp_profile'))
def view_paitent_details(request, pk):
	instance=get_object_or_404(PaitentDetails, pk=pk)
	context={
	    "paitent":instance
	}
	return render(request, 'booking/show_paitent_details.html',context=context)

@login_required(login_url=('rmp:login_rmp_profile'))
def load_time(request):
	print('**')
	date_id = request.GET.get('date')
	print(date_id)
	slots = Slot.objects.filter(date_id=date_id).filter(slot_status=False)
	print(slots)
	return render(request, 'booking/slot_dropdown_list_options.html', {'slots': slots})


class AppointmentDetialsCreate(CreateView):
	model=AppointmentDetials
	form_class = AppointmentCreateForm
	other_variable=None
	# fields=['doctor_id','appointment_id','paitent','date','time','transaction_id']
	#################################TO PASS INITIAL VALUES ############
	def get_form_kwargs(self):
		self.pk=self.kwargs['pk']
		#user = request.user
		instance=get_object_or_404(PaitentDetails,pk=self.pk)
		self.doctor_id=instance.doctor_id
		doctor_id=self.doctor_id
		kwargs = super(AppointmentDetialsCreate, self).get_form_kwargs()
		kwargs.update({'other_variable': self.doctor_id})
		return kwargs

	def get_initial(self):
		pass

	def form_valid(self, form):
		user=self.request.user
		appointment = form.save(commit=False)
		print('##')
		print(appointment)

		self.pk=self.kwargs['pk']

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
		instance=get_object_or_404(PaitentDetails,pk=self.pk)

		self.doctor_id=instance.doctor_id
		appointment.user=user
		appointment.doctor_id=self.doctor_id
		appointment.appointment_id=appointment_id
		appointment.paitent=instance
		appointment.transaction_id=transaction_id
		appointment.viedo_chat_link=viedo_chat_link
		date=appointment.date
		time=appointment.time
		slots = Slot.objects.filter(date_id=date).filter(start_time=time).first()
		slots.slot_status=True
		slots.save()
		appointment.save()

		context={

		    "object":appointment,
		}
		return render(self.request,'booking/booking_confirmation.html', context=context)
		# return super(AppointmentDetialsCreate, self).form_valid(form)


def booking_confirmation(request, pk):
	print("**")
	user=request.user
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
	obj=AppointmentDetials.objects.create(user=user,viedo_chat_link=viedo_chat_link,transaction_id=transaction_id,appointment_id=appointment_id,doctor_id=doctor_id,paitent=instance)
	obj.save()

	context={
	   "paitent":instance,
	    "object":obj,
	}
	return render(request,'booking/booking_confirmation.html', context=context)
