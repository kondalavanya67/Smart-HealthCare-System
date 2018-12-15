from django import forms
from django.conf import settings
import requests

class DiseaseForm(forms.Form):
    disease = forms.CharField(max_length=100)

    def search(self):
        result={}
        disease = self.cleaned_data['disease']
        endpoint="https://disease-info-api.herokuapp.com/diseases/{disease_id}.json"
        url = endpoint.format(disease_id=disease)
        response = requests.get(url)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % disease
            else:
                result['message'] = 'The Disease API is not available at the moment. Please try again later.'
        return result
