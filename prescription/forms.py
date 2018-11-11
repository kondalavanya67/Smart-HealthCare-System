from django import forms
from .models import Prescription, Item
from dal import autocomplete
from .models import Medicine
class Make_Prescription(forms.ModelForm):
    class Meta:
        model=Prescription
        fields='__all__'

class ItemForm(forms.ModelForm):
    medicine_name = forms.ModelChoiceField(
                queryset=Medicine.objects.all(),
                widget=autocomplete.ModelSelect2(url='prescription:name-autocomplete',
                attrs={
                'data-placeholder': 'Medicine-name',
                #'data-minimum-input-length': 1,
                })
            )
    class Meta:
        model = Item
        fields = '__all__'
