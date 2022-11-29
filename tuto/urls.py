from django.urls import path
from . import views

urlpatterns = [
    path('heroku_django/', views.django_heroku)
]
