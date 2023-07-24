from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistrarseForm
from django.urls import reverse
from django.contrib.auth import login

# Create your views here.

# Vista basada en una clase para crear a un usuario
class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistrarseForm 

    def get_success_url(self):  # Esto es para que vuelva a pagina Inicio o Index.
        return reverse('index') 
    
    def form_valid(self, form):
        respuesta = super().form_valid(form)
        usuario = form.save()
        login(self.request, usuario)
        return respuesta