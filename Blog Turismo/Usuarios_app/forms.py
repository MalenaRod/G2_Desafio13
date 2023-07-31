from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from django import forms


# Clase que crea un formulario
class RegistrarseForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email','imagen','sobre_mi']

        widgets={
            'sobre_mi': forms.Textarea(attrs= {'class':'form-control', 'placeholder': 'Si queres, contanos un poco sobre vos'}),                            
        }


class EditarUsuarioForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'imagen', 'sobre_mi']

