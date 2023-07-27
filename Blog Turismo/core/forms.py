from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'correo', 'pais', 'edad', 'mensaje']

    PAISES_CHOICES = [
        ('Argentina', 'Argentina'),
        ('Brasil', 'Brasil'),
        ('Chile', 'Chile'),
        # Agrega más países según tu preferencia...
    ]

    pais = forms.ChoiceField(choices=PAISES_CHOICES)