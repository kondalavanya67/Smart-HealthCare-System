from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from booking.models import PaitentDetails, AppointmentDetials
from doctor_profile.models import Profile, Slot
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required(login_url=reverse_lazy('login'))
def index(request):
    user=request.user
    profile = Profile.objects.get(user=user)
    appointments=AppointmentDetials.objects.filter(doctor_id=profile.id).filter(is_attended=False).order_by('date').order_by('time')
    first_name=profile.first_name
    last_name=profile.last_name
    print(user)
    print(appointments)
    #print(prescriptions[0].pdf)
    #print(prescriptions[0].prescription_date)
    if not appointments:
        context="Hurray No Pending Appointments"
    else:
        context="Pending Appointments"
    # print(appointments[0].date)
    # print(appointments[0].time)
    return render(request,'appointments.html',{'context':context,'appointments':appointments,'first_name':first_name,'last_name':last_name})

@login_required(login_url=reverse_lazy('login'))
def show_slots(request):
    user=request.user
    profile = Profile.objects.get(user=user)
    first_name=profile.first_name
    last_name=profile.last_name
    dates=Slot.objects.filter(doctor=profile)
    return render(request,'slots.html',{'slots':dates,'first_name':first_name,'last_name':last_name})
