from django.shortcuts import render


def django_heroku(request):
    return render(request, 'tuto/django_heroku.html')


def django_project(request):
    return render(request, 'tuto/django_project.html')


def git_practical(request):
    return render(request, 'tuto/git_practical.html')
