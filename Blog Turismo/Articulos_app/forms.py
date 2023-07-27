from django import forms
from .models import Publicacion, Comentario

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ('titulo', 'contenido', 'imagen', 'categoria')
        labels = {
            'titulo': '',
            'contenido': '',
            'categoria': 'Categoría'
        }        


        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese el título', 'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'placeholder': 'Escriba el articulo', 'class': 'form-control', 'rows': 4}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)
        