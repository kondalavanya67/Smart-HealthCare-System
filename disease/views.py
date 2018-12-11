from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse,reverse_lazy
import requests
from .forms import DiseaseForm

def home(request,string):
    result={}
    url="https://disease-info-api.herokuapp.com/diseases/"+str(string)+".json"
    response = requests.get(url)
    # if response.status_code == 200:
    #         result = response.json()
    #         result['success'] = True
    #     else:
    #         result['success'] = False
    #         if response.status_code == 404:
    #             result['message'] = 'No entry found for "%s"' % word
    #         else:
    #             result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
    #     return result
    result=response.json()
    print(result)
    print(string)
    return HttpResponse('ok')

def disease(request):
    search_result = {}
    if 'word' in request.GET:
        form = DiseaseForm(request.GET)
        if form.is_valid():
            search_result = form.search()
            print('**')
            print(search_result)

    else:
        form = DiseaseForm()
    print('$$')
    return render(request, 'disease/disease.html', {'form': form, 'search_result': search_result})
