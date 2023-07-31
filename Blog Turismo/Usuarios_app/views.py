from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Usuario
from .forms import RegistrarseForm
from django.urls import reverse
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import EditarUsuarioForm

#from django.shortcuts import render, get_object_or_404, redirect
#from .models import Usuario

#from django.views.generic.edit import UpdateView
#from .models import Usuario

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


class EditarUsuarioView(UpdateView):
    model = Usuario
    template_name = 'usuarios/editar-usuario.html'
    form_class = EditarUsuarioForm
    success_url = reverse_lazy('index')  # Redirige a la pagina de Inicio cuando la edición sea exitosa

class PerfilUsuarioView(DetailView):
    model = Usuario 
    template_name = 'usuarios/perfil.html'

