from django.shortcuts import render
from .forms import ApiForm
import requests
import json

def django_heroku(request):
    return render(request, 'tuto/django_heroku.html')


def django_project(request):
    return render(request, 'tuto/django_project.html')


def git_practical(request):
    return render(request, 'tuto/git_practical.html')


def cons_api(request):
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            r = requests.post('https://muti-inputs-api-multi-input.cpyusm.easypanel.host/predict', json=form.cleaned_data)
            print(form.cleaned_data)
            form.save()
            r = json.loads(r.text)
            return render(request, 'tuto/cons_api.html', context = {'form':form, 'response' : r})
    else :
        form = ApiForm()
    return render(request, 'tuto/cons_api.html', context = {'form':form})