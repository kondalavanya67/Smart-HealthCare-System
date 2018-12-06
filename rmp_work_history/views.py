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
  
    
    return render(request,'rmp_work_history/index.html',context=context)

def history(request):
    user=request.user
    appointments1 = AppointmentDetials.objects.filter(user=user).filter(is_attended=True)
    context={
        "appointments1":appointments1,
    }
    
    return render(request,'rmp_work_history/history.html',context=context)


