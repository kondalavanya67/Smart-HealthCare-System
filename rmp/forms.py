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
    email=forms.CharField(widget=forms.EmailInput)
    class Meta:
        model=rmpContact
        fields='__all__'

       


		

