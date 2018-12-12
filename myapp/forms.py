from django import forms

from myapp.models import ContactForm,NewsLetter


class contactForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    mobile_no = forms.IntegerField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = ContactForm
        fields = ['first_name','last_name','email','mobile_no','message',]

class newsLetter(forms.ModelForm):
	name = forms.CharField(required=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = NewsLetter
		fields = ['name','email',]