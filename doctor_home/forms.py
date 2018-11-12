from django import forms
from .models import login, register
from django.contrib.auth import get_user_model

User= get_user_model()

class LoginForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=login
		fields='__all__'

class RegisterForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	password1=forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
	class Meta:
   		model=register
   		fields='__all__'
	def clean_username(self):
		username=self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username is not available please take other")
		return username
	def clean_email(self):
		email=self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is not available please take other")
		return email
	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get('password')
		password1=self.cleaned_data.get('password1')
		if password1 != password:
			raise forms.ValidationError("Passwords are not matching!!!!!!") 
		return data
