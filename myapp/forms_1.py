from django import forms
from .models import animal
from django.forms import ModelForm



class AnimalForm (forms.ModelForm):
    class Meta:
        model=animal
        fields=['name' , 'kingdom' , 'sex','description','age']
