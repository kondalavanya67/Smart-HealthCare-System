from django import forms
from .models import Profile,BookingDate,Slot
# from pyuploadcare.dj.models import ImageField
class Add_Profile(forms.ModelForm):
    email_id=forms.CharField(widget=forms.EmailInput)
#     user = forms.CharField(
#     widget=forms.TextInput(attrs={'readonly':'readonly'})
# )
    class Meta:
        model=Profile
        fields='__all__'

class Modify_Profile(forms.ModelForm):
    email_id=forms.CharField(widget=forms.EmailInput)
    # profile_photo= ImageField(blank=True, manual_crop="")
    class Meta:
        model=Profile
        exclude=('user','gender','speciality',)
class SlotForm(forms.ModelForm):

    class Meta:
        model = Slot
        fields = '__all__'
