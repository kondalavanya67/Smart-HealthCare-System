from django import forms
from .models import PaitentDetails,AppointmentDetials
from doctor_profile.models import BookingDate

class Add_PaitentDetails(forms.ModelForm):
    class Meta:
        model=PaitentDetails
        fields='__all__'
        exclude=('user','doctor_id','doctor_name',)

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        if len(str(mobile_no)) != 10:
            raise forms.ValidationError('enter  a 10 digit number')
        return self.cleaned_data['mobile_no']

    def clean_symptoms(self):
        symptoms = self.cleaned_data['symptoms']
        if len(str(symptoms)) < 10:
            raise forms.ValidationError('Symptoms should be atleast 10 characters long')
        return self.cleaned_data['symptoms']

class Add_PatientToAppointment(forms.ModelForm):
    class Meta:
        model = AppointmentDetials
        fields='__all__'

class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model=AppointmentDetials
        #fields=['doctor_id','appointment_id','paitent','date','time','transaction_id','viedo_chat_link']
        fields=['date','time']

    def __init__(self, *args, **kwargs):
        doctor_id = kwargs.pop('other_variable')

        super(AppointmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['date'] = forms.ModelChoiceField(
            queryset=BookingDate.objects.filter(doctor=doctor_id)
        )
