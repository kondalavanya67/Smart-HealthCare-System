from django import forms
from .models import PaitentDetails

class Add_PaitentDetails(forms.ModelForm):
    class Meta:
        model=PaitentDetails
        fields='__all__'
