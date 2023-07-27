from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import MensajeContacto
from .forms import ContactoForm

# Create your views here.

def indexView(request):
	return render(request, 'index.html', {} )

#vista contactenos

#def vistaContactenos(request):
 #   return render(request, 'contacto.html', {})

def vistaAcerca(request):
    return render(request, 'acerca.html', {})


# contacto/views.py
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ContactoForm

class ContactoCreateView(CreateView):
    template_name = 'contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto_exitoso')  # URL a la que redireccionar después de enviar el formulario

def contacto_exitoso(request):
    return render(request, 'contacto_exitoso.html', {})