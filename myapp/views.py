from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from booking.models import AppointmentDetials,PaitentDetails
from prescription.models import Prescription
from .models import Post, Rmplist
from doctor_profile.models import Profile,Slot
from rmp.models import rmpContact
from booking.models import AppointmentDetials
# Create your views here.


def index(request):

        all_data = Post.objects.all()
        return render(request, 'myapp/index.html', {'all_data': all_data})
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
            'profile_photo':u.doctor_name.profile_photo,
            'dob':u.doctor_name.dob,
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
        user = request.user
        profile = Profile.objects.get(user=user)
        appointments = AppointmentDetials.objects.filter(doctor_id=profile.id).filter(is_attended=False)
        first_name = profile.first_name
        last_name = profile.last_name
        print(user)
        print(appointments)
        if not appointments:
            context = "No Appointments"
        else:
            context = " "
        return render(request, 'myapp/appointment.html',
                      {'context': context, 'appointments': appointments, 'first_name': first_name,
                       'last_name': last_name})


def fullappointment(request):
    if (request.method == "POST"):
        name = request.POST['booking']
        u = appointment.objects.get(patient_name=PaitentDetails.objects.get(user=User.objects.get(username=name)))
        return render(request, 'myapp/fullappointment.html', {
            'first_name': u.patient_name.first_name,
            'last_name': u.patient_name.last_name,
            'age': u.patient_name.age,
            'gender': u.patient_name.gender,
            'mobile_no':u.patient_name.mobile_no,
            'symptoms':u.patient_name.symptoms,
            'description_of_illness':u.patient_name.description_of_illness,

        })
    else:
        all_data = Post.objects.all()
        return render(request, 'myapp/fullappointment.html', {'all_data': all_data})

def doc_work_history(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    prescriptions = Prescription.objects.filter(doctor=profile)
    first_name = profile.first_name
    last_name = profile.last_name
    print(user)
    print("**")
    # print(prescriptions[0].pdf)
    # print(prescriptions[0].prescription_date)

    return render(request, 'myapp/fullappointment.html',
                  {'prescriptions': prescriptions, 'first_name': first_name, 'last_name': last_name})


def feedback(request):
    return render(request, 'myapp/feedback.html')
