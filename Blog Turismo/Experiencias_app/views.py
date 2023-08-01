from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .models import Experiencias
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import Super_autor_mixin, Colab_Mixin
from django.http import Http404
from django.core.exceptions import PermissionDenied
from .forms import ExperienciasForm

# Create your views here.

class ListaExperiencias(ListView):
    model = Experiencias
    template_name = 'experiencias/experiencias.html'
    context_object_name = 'experiencias'
 

class AprobarExperiencia(LoginRequiredMixin, Colab_Mixin, UpdateView):
    model = Experiencias
    template_name = 'aprobar_experiencias.html'
    fields = ['aprobado', 'aprobado_por']
    success_url = reverse_lazy('experiencias:aprobar_experiencias')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.es_colaborador == 0:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data(experiencia=self.object))
    
    def form_valid(self, form):
        form.instance.aprobado = True
        form.instance.aprobado_por = self.request.user
        return super().form_valid(form)

def me_gustaView(request):
    if request.method == 'POST':
        experiencias_id = request.POST.get('experiencias_id')
        experiencia = get_object_or_404(Experiencias, id = experiencias_id)
        usuario = request.user

        if experiencia.megusta.filter(id=usuario.id).exists():
            experiencia.megusta.remove(usuario)
        else:
            experiencia.megusta.add(usuario)

    return redirect(reverse('experiencias:experiencias', kwargs={'pk':experiencias_id}))


    

class NuevaExperiencia(LoginRequiredMixin, Colab_Mixin, CreateView):
    model = Experiencias
    template_name = 'experiencias/crear_experiencias.html'
    form_class = ExperienciasForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user.id
        return super().form_valid(f)


def experiencia_creada(request):
    return render(request, 'experiencia_creada.html', {})
 

class EliminarExperiencia(LoginRequiredMixin, Colab_Mixin, DeleteView):
    template_name = 'experiencias/eliminar_experiencia.html'
    model = Experiencias
    success_url = reverse_lazy('experiencias:aprobar_experiencias')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.es_colaborador == self.request.user

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_superuser and not self.request.user.es_colaborador == self.request.user:
            raise Http404
        return obj

