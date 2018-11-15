from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from prescription.models import Prescription
from doctor_profile.models import Profile

def index(request):
    user=request.user
    profile = Profile.objects.get(user=user)
    prescriptions=Prescription.objects.filter(doctor=profile)
    print(user)
    print("**")
    print(prescriptions[0].prescription_date)

    return render(request,'work_history_home.html',{'prescriptions':prescriptions})
