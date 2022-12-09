from django.urls import path
from . import views

urlpatterns = [
    path('heroku_django/', views.django_heroku, name='django_heroku'),
    path('api_ml/', views.cons_api, name='cons_api'),
    path('django_project/', views.django_project, name='django_project'),
    path('git_practical/', views.django_project, name='git_practical'),
]
