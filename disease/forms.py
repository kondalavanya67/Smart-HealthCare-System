from django import forms
from django.conf import settings
import requests

class DiseaseForm(forms.Form):
    word = forms.CharField(max_length=100)

    def search(self):
        result={}
        word = self.cleaned_data['word']
        endpoint="https://disease-info-api.herokuapp.com/diseases/{word_id}.json"
        url = endpoint.format(word_id=word)
        response = requests.get(url)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The Disease API is not available at the moment. Please try again later.'
        return result
