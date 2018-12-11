from django import forms
from django.contrib.auth import get_user_model
from .models import rmpContact



User=get_user_model()


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

		

