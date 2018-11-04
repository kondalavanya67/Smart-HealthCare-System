from django import forms

from .models import medicine

class add_medicine_Form(forms.ModelForm):
    class Meta:
        model = medicine
        fields = [
            "name",
            "about",
            "usage",
        ]