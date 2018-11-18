from django import forms
from .models import PaitentDetails,AppointmentDetials

class Add_PaitentDetails(forms.ModelForm):
    class Meta:
        model=PaitentDetails
        fields='__all__'

class Add_PatientToAppointment(forms.ModelForm):
    class Meta:
        model = AppointmentDetials
        fields='__all__'
