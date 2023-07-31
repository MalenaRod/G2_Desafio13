from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'correo', 'pais', 'edad', 'mensaje']
        labels={
            'nombre': '',
            'correo': '',
            'pais':'',
            'edad': '',
            'mensaje':''
        }        
        
        widgets={
           'nombre': forms.TextInput(attrs= {'class':'form-control', 'placeholder': 'Nombre'}),
           'correo': forms.TextInput(attrs= {'placeholder': 'Correo electrónico', 'class':'form-control'}),
           'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
           'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deje su consulta aquí...'}),                                
        }
           

    PAISES_CHOICES = [
        ('Argentina', 'Argentina'), ('Bolivia', 'Bolivia'), ('Brasil', 'Brasil'), ('Chile', 'Chile'), ('Colombia', 'Colombia'), ('Ecuador', 'Ecuador'), ('Paraguay', 'Paraguay'), ('Perú', 'Perú'), ('Uruguay', 'Uruguay'), ('Venezuela', 'Venezuela'),  ('Centro America', 'Centro America'),  ('Europa', 'Europa'),  ('America del Norte', 'America del Norte'), ('Asia', 'Asia'), ('Otros', 'Otros'),

    ]

    pais = forms.ChoiceField(choices=PAISES_CHOICES)