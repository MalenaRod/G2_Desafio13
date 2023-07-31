from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import MensajeContacto
from .forms import ContactoForm
from django.urls import reverse_lazy
from .mixins import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from Articulos_app.models import Publicacion


def termViews(request):
    return render(request, 'termino_condiciones.html', {})
def politViews(request):
    return render(request, 'politica_privacidad.html', {})

def indexView(request):
    lista_publicaciones = Publicacion.objects.order_by('-fecha_publicacion')[:3]
    context = {
        'articulos': lista_publicaciones,
    }
    return render(request, 'index.html', context)


def vistaAcerca(request):
    return render(request, 'acerca.html', {})


# contacto/views.py

class ContactoCreateView(CreateView):
    template_name = 'contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto_exitoso') 

def contacto_exitoso(request):
    return render(request, 'contacto_exitoso.html', {})

class VerContactos(LoginRequiredMixin, Colab_Mixin, ListView):
    model = MensajeContacto
    template_name = 'mensajes_contacto.html'
    context_object_name = 'mensajes'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.es_colaborador == 0:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class AtenderContacto(LoginRequiredMixin, Colab_Mixin, UpdateView):
    model = MensajeContacto
    template_name = 'atender_mensaje.html'
    fields = ['visto', 'atendido_por']
    success_url = reverse_lazy('mensajes_contacto')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.es_colaborador == 0:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data(mensaje=self.object))
    
    def form_valid(self, form):
        form.instance.visto = True
        form.instance.atendido_por = self.request.user
        return super().form_valid(form)
    
