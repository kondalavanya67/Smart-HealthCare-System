from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post, Rmplist
from doctor_profile.models import Profile
from rmp.models import rmpContact
# Create your views here.


def index(request):
        all_data = Post.objects.all()
        return render(request, 'myapp/index.html', {'all_data':all_data})


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
    return render(request, 'myapp/appointment.html')
def feedback(request):
    return render(request, 'myapp/feedback.html')


