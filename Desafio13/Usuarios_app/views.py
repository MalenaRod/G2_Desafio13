from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistrarseForm
from django.urls import reverse

# Create your views here.

# Vista basada en una clase para crear a un usuario
class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistrarseForm #UserCreationForm (despues lo cambia)

    def get_success_url(self):  # Esto es para que vuelva a pagina Inicio o Index.
        return reverse('index') 