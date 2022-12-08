# from django import forms
from django import forms
from .models import ApiModel

class ApiForm(forms.ModelForm):
    class Meta:
        model = ApiModel
        fields = "__all__"
        labels = {
            'text' : 'Entrez votre description ici',
            'url' : 'Entrez votre url ici',
        }
