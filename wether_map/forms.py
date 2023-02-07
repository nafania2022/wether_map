from .models import *
from django.forms import ModelForm, TextInput

class SityForm(ModelForm):
    class Meta:
        model = Sity
        fields = ['name']
        widgets = {"name": TextInput(attrs={'class': 'form-control', 'placeholder':'Введите название'})}