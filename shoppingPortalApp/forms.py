from django import forms

from .models import medicine

class add_medicine_Form(forms.ModelForm):
    class Meta:
        model = medicine
        fields = [
            "name",
            "about",
            "usage",
            "image",
            "price",
            "manufacturedBy",
        ]
        
class del_medicine_Form(forms.Form):
    name_to_del = forms.CharField(max_length=25)

class update_medicine_Form(forms.Form):
    name = forms.CharField(max_length = 120)
    about = forms.CharField(max_length = 120)
    usage = forms.CharField(max_length = 120)
    manufacturedBy = forms.CharField(max_length = 120)
    price = forms.FloatField()
            
class Modify_Medicine_Form(forms.ModelForm):
    class Meta:
        model = medicine
        exclude=('image','updated',)
        