from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DoctorProfileSerializer,RmpProfileSerializer,AppointmentDetialsSerializer,PaitentDetailsSerializer,SlotSerializer
from doctor_profile.models import Profile,Slot
from rmp.models import rmpContact
from booking.models import AppointmentDetials,PaitentDetails

# Create your views here.

class DoctorProfileViewSet(viewsets.ModelViewSet):

    serializer_class = DoctorProfileSerializer

    def get_queryset(self):
        queryset = Profile.objects.all()
        qs=self.request.query_params.get("q")
        if qs is not None:
            queryset=queryset.filter(speciality=qs)
        return queryset

class RmpProfileViewSet(viewsets.ModelViewSet):

    serializer_class = RmpProfileSerializer
    def get_queryset(self):
        queryset = rmpContact.objects.all()
        qs=self.request.query_params.get("q")
        if qs is not None:
            queryset=queryset.filter(locality=qs)
        return queryset

class AppointmentDetialsViewSet(viewsets.ModelViewSet):

    serializer_class = AppointmentDetialsSerializer
    def get_queryset(self):
        queryset = AppointmentDetials.objects.all()
        qs=self.request.query_params.get("q")
        if qs is not None:
            queryset=queryset.filter(is_attended=qs)
        return queryset

class PaitentDetailsViewSet(viewsets.ModelViewSet):

    serializer_class = PaitentDetailsSerializer
    def get_queryset(self):
        queryset = PaitentDetails.objects.all()
        qs=self.request.query_params.get("q")
        if qs is not None:
            queryset=queryset.filter(is_attended=qs)
        return queryset

class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
