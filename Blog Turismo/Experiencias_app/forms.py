from django import forms
from .models import Experiencias



class ExperienciasForm(forms.ModelForm):
    model= Experiencias
    fields=('titulo', 'contenido', 'imagen')
    labels = {
            'titulo': '',
            'contenido': '',
        }        


    widgets = {
        'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese el título', 'class': 'form-control'}),
        'contenido': forms.Textarea(attrs={'placeholder': 'Escriba sobre su experiencia', 'class': 'form-control', 'rows': 4}),
        }