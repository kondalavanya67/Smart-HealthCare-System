from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from prescription.models import Prescription
from doctor_profile.models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from booking.models import AppointmentDetials
@login_required(login_url=reverse_lazy('login'))
def index1(request):
    user=request.user
    profile = Profile.objects.get(user=user)
    appointments=AppointmentDetials.objects.filter(doctor_id=profile.id).filter(is_attended=True)
    first_name=profile.first_name
    last_name=profile.last_name
    print("JKKKJK")
    # print(user)
    # print(appointments)
    # #print(prescriptions[0].pdf)
    # #print(prescriptions[0].prescription_date)
    # if not appointments:
    #     context="Hurray No Pending Appointments"
    # else:
    #     context="Pending Appointments"
    # print(appointments[0].date)
    # print(appointments[0].time)
    return render(request,'work_history_home1.html',{'appointments':appointments,'first_name':first_name,'last_name':last_name})
