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
        exclude = ('user',)

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        if len(str(mobile_no)) != 10:
            raise forms.ValidationError('enter  a 10 digit number')
        return self.cleaned_data['mobile_no']

# user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
# profile_photo=models.ImageField(upload_to='media_/profile_pic/')
# first_name=models.CharField(max_length=250)
# last_name=models.CharField(max_length=500)
# dob= models.DateField(default=date.today )
# gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
# email_id=models.CharField(max_length=250)
# mobile_no=models.BigIntegerField()
# speciality=models.CharField(max_length=250, choices=SPECIALITY_CHOICES)
# qualification=models.CharField(max_length=250)
# locality=models.CharField(max_length=250)
# hospital=models.CharField(max_length=250)




class Modify_Profile(forms.ModelForm):
    email_id=forms.CharField(widget=forms.EmailInput)
    # profile_photo= ImageField(blank=True, manual_crop="")
    class Meta:
        model=Profile
        exclude=('user','gender','speciality',)


    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        if len(str(mobile_no)) != 10:
            raise forms.ValidationError('enter  a 10 digit number')
        return self.cleaned_data['mobile_no']



class SlotForm(forms.ModelForm):

    class Meta:
        model = Slot
        fields = '__all__'
