from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('cv/', views.cv, name='cv'),
    path('projets/', views.projets, name='projets'),
    path('ressources/', views.ressources, name='ressources'),
]
