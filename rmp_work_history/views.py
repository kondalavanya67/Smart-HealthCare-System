from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from booking.models import AppointmentDetials,PaitentDetails



def index(request):
    user=request.user
    appointments = AppointmentDetials.objects.filter(user=user)
    context={
        "appointments":appointments,
    }
    print(appointments)
    
    return render(request,'rmp_work_history/index.html',context=context)
