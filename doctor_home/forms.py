from django import forms
from .models import login, register
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-label-group'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-label-group'}))
	

class RegisterForm(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-label-group'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-label-group'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-label-group'}))
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password','class': 'form-label-group'}), label='confirm_password')
	class Meta:
   		model=User
   		fields=('username','email','password','password1')
	#def clean_username(self):
	#	username=self.cleaned_data.get('username')
	#	qs = User.objects.filter(username=username)
	#	if qs.exists():
	#		raise forms.ValidationError("username is not available please take other")
	#	return username
	#def clean_email(self):
	#	email=self.cleaned_data.get('email')
	#	qs = User.objects.filter(email=email)
	#	if qs.exists():
	#		raise forms.ValidationError("email is not available please take other")
	#	return email
	def clean_confirm_password(self):
		#data=self.cleaned_data
		password=self.cleaned_data.get('password')
		confirm_password=self.cleaned_data.get('confirm_password')
		if password != confirm_password:
			raise forms.ValidationError("Passwords are not matching!!!!!!") 
		return confirm_password
