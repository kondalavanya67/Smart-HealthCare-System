from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post, Rmplist
from doctor_profile.models import Profile,Slot
from rmp.models import rmpContact
from booking.models import AppointmentDetials
# Create your views here.


def index(request):
        doctors = Profile.objects.all()
        context = {

    	   "doctor" : doctors,
    	}
        return render(request, 'myapp/index.html',context=context)

def doctor_detail(request, pk):
    instance = get_object_or_404(Profile, pk=pk)
    context = {
        "doctor" : instance,
    }
    return render(request, 'myapp/doctor_detail1.html',context=context)

def doctor_upcoming_appointments(request, pk):

    profile = get_object_or_404(Profile, pk=pk)
    appointments=AppointmentDetials.objects.filter(doctor_id=profile.id).filter(is_attended=False)

    if not appointments:
        context="Hurray No Pending Appointments"
    else:
        context="Pending Appointments"

    return render(request,'myapp/upcoming_appointments.html',{'context':context,'appointments':appointments})

def doctor_attended_appointments(request, pk):

    profile = get_object_or_404(Profile, pk=pk)
    appointments=AppointmentDetials.objects.filter(doctor_id=profile.id).filter(is_attended=True)
    #
    # if not appointments:
    #     context="Hurray No Pending Appointments"
    # else:
    #     context="Pending Appointments"

    return render(request,'myapp/attended_appointments.html',{'appointments':appointments})

def show_slots(request,pk):

    profile = get_object_or_404(Profile, pk=pk)
    first_name=profile.first_name
    last_name=profile.last_name
    dates=Slot.objects.filter(doctor=profile)
    return render(request,'myapp/slots.html',{'slots':dates})

def fullviewdoc(request):
    if (request.method == "POST"):
        name = request.POST['doctor']
        u = Post.objects.get(doctor_name=Profile.objects.get(user=User.objects.get(username=name)))
        return render(request,'myapp/fullviewdoc.html',{
            'first_name': u.doctor_name.first_name,
            'last_name' : u.doctor_name.last_name,
            'gender' : u.doctor_name.gender,
            'email_id': u.doctor_name.email_id,
            'speciality': u.doctor_name.speciality,
            'qualification': u.doctor_name.qualification,
            'mobile_no': u.doctor_name.mobile_no,
            'locality': u.doctor_name.locality,
            'hospital': u.doctor_name.hospital,
        })
    else:
        all_data = Post.objects.all()
        return render(request, 'myapp/fullviewdoc.html', {'all_data': all_data})

def rmpdetails(request):
    doctors = rmpContact.objects.all()
    context = {

       "doctor" : doctors,
    }
    return render(request, 'myapp/rmplist.html',context=context)


def fullviewrmp(request, pk):
    instance = get_object_or_404(rmpContact, pk=pk)
    context = {
        "profile" : instance,
    }
    return render(request, 'myapp/fullviewrmp.html',context=context)


def adminpage(request):
    return render(request, 'myapp/adminpage.html')


def payment(request):
    return render(request, 'myapp/payment.html')
def appointment(request):
    return render(request, 'myapp/appointment.html')
def feedback(request):
    return render(request, 'myapp/feedback.html')


def rmp_appointments_past(request,pk):
    appointments = AppointmentDetials.objects.filter(user=pk)
    context={
        "appointments":appointments,
    }
    
    return render(request,'myapp/rmp_appointments_past.html',context=context)

