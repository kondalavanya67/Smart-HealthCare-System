from django import forms
from django.contrib.auth import get_user_model
from .models import rmpContact



User=get_user_model()


class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	username=forms.CharField()
	email=forms.EmailField()
	password=forms.CharField(widget=forms.PasswordInput())
	password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
    
	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get("password")
		password2=self.cleaned_data.get("password2")
		if password2 != password:
			raise forms.ValidationError("Passwords donot match")
		return data



       
class Add_Rmp_Profile(forms.ModelForm):
    email_id=forms.CharField(widget=forms.EmailInput)
    class Meta:
        model=rmpContact
        exclude = ('user',)

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        if len(str(mobile_no)) != 10:
            raise forms.ValidationError('enter  a 10 digit number')
        return self.cleaned_data['mobile_no']

		

