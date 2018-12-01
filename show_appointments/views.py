from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from booking.models import PaitentDetails, AppointmentDetials
from doctor_profile.models import Profile, Slot

def index(request):
    user=request.user
    profile = Profile.objects.get(user=user)
    appointments=AppointmentDetials.objects.filter(doctor_id=profile.id)
    first_name=profile.first_name
    last_name=profile.last_name
    print(user)
    print("**")
    #print(prescriptions[0].pdf)
    #print(prescriptions[0].prescription_date)

    return render(request,'appointments.html',{'appointments':appointments,'first_name':first_name,'last_name':last_name})

def show_slots(request):
    user=request.user
    profile = Profile.objects.get(user=user)
    first_name=profile.first_name
    last_name=profile.last_name
    dates=Slot.objects.filter(doctor=profile)
    return render(request,'slots.html',{'slots':dates,'first_name':first_name,'last_name':last_name})
