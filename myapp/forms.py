from django import forms
from .models import animal
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget #add ckeditor of fields



class AnimalForm (forms.ModelForm):
    description= forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=animal
        fields=['name' , 'kingdom' , 'sex','description','age','img']
