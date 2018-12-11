from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DoctorProfileSerializer,RmpProfileSerializer,AppointmentDetialsSerializer,PaitentDetailsSerializer,SlotSerializer
from doctor_profile.models import Profile,Slot
from rmp.models import rmpContact
from booking.models import AppointmentDetials,PaitentDetails

# Create your views here.

class DoctorProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = DoctorProfileSerializer

class RmpProfileViewSet(viewsets.ModelViewSet):
    queryset = rmpContact.objects.all()
    serializer_class = RmpProfileSerializer

class AppointmentDetialsViewSet(viewsets.ModelViewSet):
    queryset = AppointmentDetials.objects.all()
    serializer_class = AppointmentDetialsSerializer

class PaitentDetailsViewSet(viewsets.ModelViewSet):
    queryset = PaitentDetails.objects.all()
    serializer_class = PaitentDetailsSerializer

class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer



