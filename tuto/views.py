from django.shortcuts import render

# Create your views here.


def django_heroku(request):
    return render(request, 'tuto/django_heroku.html')
