from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import MensajeContacto
from .forms import ContactoForm
from django.views.generic import ListView
# Create your views here.
from Articulos_app.models import Publicacion

class lista_publicacioness(ListView):
    model = Publicacion
    template_name = 'index.html'
    context_object_name = 'articulos'
    paginate_by = 3

def indexView(request):
    lista_publicaciones = Publicacion.objects.order_by('-fecha_publicacion')[:3]
    context = {
        'articulos': lista_publicaciones,
    }
    return render(request, 'index.html', context)


def vistaAcerca(request):
    return render(request, 'acerca.html', {})


# contacto/views.py
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ContactoForm

class ContactoCreateView(CreateView):
    template_name = 'contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto_exitoso') 

def contacto_exitoso(request):
    return render(request, 'contacto_exitoso.html', {})