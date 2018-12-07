from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from booking.models import AppointmentDetials,PaitentDetails
from prescription.models import Prescription
from .models import Post, Rmplist
from doctor_profile.models import Profile
from rmp.models import rmpContact
# Create your views here.


def index(request):
        all_data = Post.objects.all()
        return render(request, 'myapp/index.html', {'all_data': all_data})


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
        data = Rmplist.objects.all()
        return render(request, 'myapp/rmplist.html', {'data':data})


def fullviewrmp(request):
    if (request.method == "POST"):
        name = request.POST['rmp']
        u = Rmplist.objects.get(rmp_list=rmpContact.objects.get(user=User.objects.get(username=name)))
        return render(request,'myapp/fullviewrmp.html',{
            'first_name': u.rmp_list.first_name,
            'last_name' : u.rmp_list.last_name,
            'gender' : u.rmp_list.gender,
            'email_id': u.rmp_list.email_id,
            'qualification': u.rmp_list.qualification,
            'mobile_no': u.rmp_list.mobile_no,
            'locality': u.rmp_list.locality,
            'hospital': u.rmp_list.hospital,
        })
    else:
        all_data = Post.objects.all()
        return render(request, 'myapp/fullviewdoc.html', {'all_data': all_data})


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


