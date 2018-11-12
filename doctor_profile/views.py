from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Profile
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import Add_Profile
# Create your views here.
def index(request):
    return render(request,'profile_home.html')
###############DJANGO FORMS ##############
def make_profile(request):
    if request.method=="POST":
        form=Add_Profile(request.POST, request.FILES)
        if form.is_valid():
            profile_item=form.save(commit=False)
            profile_item.save()
            return redirect('/profile/show_profile/'+str(profile_item.doctor_id))
    else:
        form=Add_Profile()
    return render(request,'new.html',{'form':form})

def modify_profile(request,doctor_id):
    profile_item=get_object_or_404(Profile,doctor_id=doctor_id)
    form=Add_Profile(request.POST or None, instance=profile_item)
    if form.is_valid():
            form.save()
            return redirect('/profile/show_profile/'+str(profile_item.doctor_id))
    return render(request,'new.html',{'form':form})

def Show_Profile(request,doctor_id):
        profile=get_object_or_404(Profile,doctor_id=doctor_id)
        context={
            'profile':profile
        }
        return render(request,'show_profile.html',context)
'''
def make_profie(request):
    return render(request,'make_profile.html')

def add_profile(request):
    doctor_id=request.POST['doctor_id']
    profile_pic=request.POST['profile_photo']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    gender=request.POST['gender']
    mobile_no=request.POST['mobile_no']
    speciality=request.POST['speciality']
    qualification=request.POST['qualification']
    locality=request.POST['locality']
    hospital=request.POST['hospital']

    profile=Profile.objects.create(doctor_id=doctor_id,profile_photo=profile_pic,first_name=first_name,last_name=last_name,gender=gender,email_id=email,mobile_no=mobile_no,speciality=speciality,qualification=qualification,locality=locality,hospital=hospital)

    context={
        'profile':profile
    }
    return render(request,'show_profile.html',context)
    #return HttpResponse("CONGRATS Dr.{} {} ".format(first_name,last_name))

def modify_profile(request,profile_id):
    profile=get_object_or_404(Profile,userid=userid)
    context={
        'profile':profile,

    }
    return render(request,'modify_profile.html',context)

def Modify_Profile_Databse(request):
    doctor_id=request.POST['doctor_id']
    profile_pic=request.POST['profile_photo']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    gender=request.POST['gender']
    mobile_no=request.POST['mobile_no']
    speciality=request.POST['speciality']
    qualification=request.POST['qualification']
    locality=request.POST['locality']
    hospital=request.POST['hospital']

    profile=get_object_or_404(Profile,userid=userid)
    profile.profile_pic-profile_pic
    profile.first_name=first_name
    profile.last_name=last_name
    profile.email_id=email
    profile.gender=gender
    profile.mobile_no=mobile_no
    profile.speciality=speciality
    profile.qualification=qualification
    profile.locality=locality
    profile.hospital=hospital



'''
