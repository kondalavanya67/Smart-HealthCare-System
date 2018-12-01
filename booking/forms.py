from django import forms
from .models import PaitentDetails,AppointmentDetials
from doctor_profile.models import BookingDate,Profile,Slot
from django.shortcuts import render,get_object_or_404,redirect
class Add_PaitentDetails(forms.ModelForm):
    class Meta:
        model=PaitentDetails
        fields='__all__'

class Add_PatientToAppointment(forms.ModelForm):
    class Meta:
        model = AppointmentDetials
        fields='__all__'

class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model=AppointmentDetials
        fields=['doctor_id','appointment_id','paitent','date','time','transaction_id','viedo_chat_link']

    def __init__(self, *args, **kwargs):
        doctor_id = kwargs.pop('other_variable')
        # doctor=get_object_or_404(Profile,pk=doctor_id)
        # print('**')
        # print(doctor_id)
        super(AppointmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['date'] = forms.ModelChoiceField(
            queryset=BookingDate.objects.filter(doctor=doctor_id)
        )
        self.fields['time'].queryset = Slot.objects.none()
        # date_id = str(self.data.get('date'))
        # self.fields['time'].queryset = Slot.objects.filter(date=date_id)
        # print('&&')
        # if 'date' in self.data:
        #     print('&&')
        #     try:
        #         print('**')
        #         date_id = int(self.data.get('date'))
        #         self.fields['time'].queryset = Slots.objects.filter(date_id=date_id)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # else :
        #     print('XX')
        #     self.fields['time'].queryset = Slots.objects.all()
        # date=self.fields['date']
        # print(type(date))
        # elf.fields['date'] = forms.ModelChoiceField(
        #     queryset=BookingDate.objects.filter(date=str(date))
        # )
        # print('**')
        # print(date)

    # def __init__(self, *args, **kwargs):
    #     doctor_id = kwargs.pop('other_variable')
    #     super(MyForm, self).__init__(*args, **kwargs)



    # def __init__(self, *args, **kwargs):
    #     super(AppointmentCreateForm, self).__init__(self, *args, **kwargs)
    #     doctor=get_object_or_404(Profile,pk=self.doctor_id)
    #     self.fields['date'].queryset = BookingDate.objects.filter(date='2018-12-03')
