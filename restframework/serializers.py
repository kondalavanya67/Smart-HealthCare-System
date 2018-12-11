from rest_framework import serializers
from doctor_profile.models import Profile,Slot
from rmp.models import rmpContact
from booking.models import AppointmentDetials,PaitentDetails

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__'


class RmpProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = rmpContact
        fields='__all__'

class AppointmentDetialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDetials
        fields='__all__'

class PaitentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaitentDetails
        fields='__all__'

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields='__all__'

