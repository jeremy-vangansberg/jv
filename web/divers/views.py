from django.shortcuts import render

def home_page(request):
    return render(request, 'divers/home_page.html')

def cv(request):
    return render(request, 'divers/cv.html')

def projets(request):
    return render(request, 'divers/projets.html')

def ressources(request):
    return render(request, 'divers/ressources.html')