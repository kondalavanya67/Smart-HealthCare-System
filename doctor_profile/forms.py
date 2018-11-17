from django import forms
from .models import Profile
class Add_Profile(forms.ModelForm):
    email_id=forms.CharField(widget=forms.EmailInput)
    
    class Meta:
        model=Profile
        fields='__all__'
