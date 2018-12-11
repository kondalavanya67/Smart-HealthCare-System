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
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-label-group'}))
	class Meta:
   		model=User
   		fields=('username','email','password','password1')
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
	def clean_password1(self):
		#data=self.cleaned_data
		password=self.cleaned_data.get('password')
		password1=self.cleaned_data.get('password1')
		if password != password1:
			raise forms.ValidationError("Passwords are not matching!!!!!!") 
		return password1

#class ResetForm(forms.ModelForm):
#	email=forms.EmailField(widget=forms.TextInput(attrs={'autocomplete':'off'}))
#	class Meta:
#		model=User
#		fields=('email',)
#	def clean(self):
#		cleaned_data=super().clean()
#		email=cleaned_data.get("email")
##		email_set=User.objects.filter(email=email)
#
#		if not email_set.exists():
#			raise forms.ValidationError('Email is not yet registered.')
#			return email

