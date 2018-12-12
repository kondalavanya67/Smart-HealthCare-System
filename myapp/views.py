from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from booking.models import AppointmentDetials,PaitentDetails
from myapp.forms import ContactForm,NewsLetter
from prescription.models import Prescription
from .models import Post, Rmplist
from doctor_profile.models import Profile,Slot
from rmp.models import rmpContact
from booking.models import AppointmentDetials
from shopping_cart.models import Order
from payment.models import OnlinePayment
# Create your views here.

@login_required(login_url=reverse_lazy('login_admin'))
def index(request):

        doctors = Profile.objects.filter(verified=True)
        context = {

        "doctor" : doctors,
    }
    return render(request, 'myapp/index.html',context=context)

def doctor_verify(request):
        doctors = Profile.objects.filter(verified=False)
        print('%%')
        context = {

    	   "doctor" : doctors,
    	}
        return render(request, 'myapp/doctor_verify.html',context=context)

@login_required(login_url=reverse_lazy('login_admin'))
def doctor_detail(request, pk):
    instance = get_object_or_404(Profile, pk=pk)
    context = {
        "doctor" : instance,
    }
    return render(request, 'myapp/doctor_detail1.html',context=context)

@login_required(login_url=reverse_lazy('login_admin'))
def doctor_upcoming_appointments(request, pk):

    profile = get_object_or_404(Profile, pk=pk)
    appointments=AppointmentDetials.objects.filter(doctor_id=profile.id).filter(is_attended=False)

    if not appointments:
        context="Hurray No Pending Appointments"
    else:
        context="Pending Appointments"

    return render(request,'myapp/upcoming_appointments.html',{'context':context,'appointments':appointments})

@login_required(login_url=reverse_lazy('login_admin'))
def doctor_attended_appointments(request, pk):

    profile = get_object_or_404(Profile, pk=pk)
    appointments=AppointmentDetials.objects.filter(doctor_id=profile.id).filter(is_attended=True)
    #
    # if not appointments:
    #     context="Hurray No Pending Appointments"
    # else:
    #     context="Pending Appointments"

    return render(request,'myapp/attended_appointments.html',{'appointments':appointments})

@login_required(login_url=reverse_lazy('login_admin'))
def show_slots(request,pk):

    profile = get_object_or_404(Profile, pk=pk)
    first_name=profile.first_name
    last_name=profile.last_name
    dates=Slot.objects.filter(doctor=profile)
    return render(request,'myapp/slots.html',{'slots':dates})

def doctor_verify_confirmation(request,pk):

    print('**')
    print("hello")
    profile = get_object_or_404(Profile, pk=pk)
    print('**')
    profile.verified=True
    profile.save()
    return redirect(reverse("myapp:doctor_verify"))

@login_required(login_url=reverse_lazy('login_admin'))
def rmpdetails(request):
    doctors = rmpContact.objects.all()
    context = {

        "doctor" : doctors,
    }
    return render(request, 'myapp/rmplist.html',context=context)

@login_required(login_url=reverse_lazy('login_admin'))
def fullviewrmp(request, pk):
    instance = get_object_or_404(rmpContact, pk=pk)
    context = {
        "profile" : instance,
    }
    return render(request, 'myapp/fullviewrmp.html',context=context)

@login_required(login_url=reverse_lazy('login_admin'))
def adminpage(request):
    return render(request, 'myapp/adminpage.html')



@login_required(login_url=reverse_lazy('login_admin'))
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

@login_required(login_url=reverse_lazy('login_admin'))
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

@login_required(login_url=reverse_lazy('login_admin'))
def rmpdetail(request):
    instance = get_object_or_404(rmpContact)
    context = {
        "profile": instance,
    }
    return render(request, 'myapp/rmp_detail.html', context=context)

@login_required(login_url=reverse_lazy('login_admin'))
def rmp_upcoming_appointments(request, pk):
    profile = get_object_or_404(rmpContact, pk=pk)
    appointments = AppointmentDetials.objects.filter(user=profile.user).filter(is_attended=False)
    if not appointments:
        context = "Hurray No Pending Appointments"
    else:
        context = "Pending Appointments"

    return render(request,'myapp/rmp_upcoming_appointments.html',{'context':context,'appointments':appointments})

@login_required(login_url=reverse_lazy('login_admin'))
def rmp_attended_appointments(request, pk):
    profile = get_object_or_404(rmpContact, pk=pk)
    appointments = AppointmentDetials.objects.filter(user=profile.user).filter(is_attended=True)
    return render(request,'myapp/rmp_attended_appointments.html',{'appointments':appointments})

@login_required(login_url=reverse_lazy('login_admin'))
def patientdetails(request, pk):
    instance = get_object_or_404(rmpContact, pk=pk)
    paitents = PaitentDetails.objects.filter(user=instance.user)
    context = {
        "paitents": paitents,
        "instance":instance,
    }
    return render(request,'myapp/details.html',context=context)

@login_required(login_url=reverse_lazy('login_admin'))
def feedback(request):
    feedback = ContactForm.objects.all()
    context = {
        "feedback" : feedback,
    }
    return render(request, 'myapp/feedback.html',context=context)

def newsletter(request):
    feedback1 = NewsLetter.objects.all()
    context = {
        "feedback1" : feedback1,
    }
    return render(request, 'myapp/newsletters.html',context=context)

def rmp_appointments_past(request,pk):
    appointments = AppointmentDetials.objects.filter(user=pk)
    context={
        "appointments":appointments,
    }

    return render(request,'myapp/rmp_appointments_past.html',context=context)

def shop_history(request):
    orders = Order.objects.all()
    return render(request,'myapp/total_order.html',{'orders':orders,})

@login_required(login_url=reverse_lazy('login_admin'))
def payment(request):
    payment_history = OnlinePayment.objects.all()
    return render(request, 'myapp/payment.html',{'payments' : payment_history,})
