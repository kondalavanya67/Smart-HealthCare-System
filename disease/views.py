from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse,reverse_lazy
import requests
from .forms import DiseaseForm

def disease(request):
    search_result = {}
    if 'disease' in request.GET:
        form = DiseaseForm(request.GET)
        if form.is_valid():
            search_result = form.search()
            print('**')
            print(search_result)

    else:
        form = DiseaseForm()
    print('$$')
    return render(request, 'disease/disease.html', {'form': form, 'search_result': search_result})
