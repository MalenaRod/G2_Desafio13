from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicacion, Categoria, Comentario
from .forms import PublicacionForm, ComentarioForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import Super_autor_mixin, Colab_Mixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class lista_publicaciones(ListView):
    model = Publicacion
    template_name = 'articulos/lista_publicaciones.html'
    context_object_name = 'articulos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        #Filtro por categoria
        categoria_seleccionada = self.request.GET.get('categoria')
        if categoria_seleccionada:
            queryset = queryset.filter(categoria = categoria_seleccionada)
        
        # Orden
        orden = self.request.GET.get('orden')
        if orden:
            if orden == 'fecha_asc':
                queryset = queryset.order_by('fecha')
            elif orden == 'fecha_desc':
                queryset = queryset.order_by('-fecha')
            elif orden == 'alf_asc':
                queryset = queryset.order_by('titulo')
            elif orden == 'alf_desc':
                queryset = queryset.order_by('-titulo')


        return queryset


class detalle_publicacion(FormView):
    template_name = "articulos/detalle_publicacion.html"
    form_class = ComentarioForm
    
    def get_success_url(self):
        return reverse_lazy('articulos:detalle_publicacion', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulo'] = Publicacion.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('usuarios:login')
        comentario = form.save(commit=False)
        comentario.autor = self.request.user
        comentario.contenido = Publicacion.objects.get(pk=self.kwargs['pk'])
        comentario.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    
class BorrarComentario(Super_autor_mixin, LoginRequiredMixin,DeleteView):
    model=Comentario
    template_name= 'articulos/borrar-comentario.html'

    def get_success_url(self):
        return reverse('articulos:detalle_publicacion', args=[self.object.contenido.id])

class nueva_publicacion(LoginRequiredMixin, Colab_Mixin, CreateView):
    model = Publicacion
    template_name = 'articulos/nueva_publicacion.html'
    form_class = PublicacionForm

    def get_success_url(self):
        return reverse('articulos:lista_publicaciones')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user.id
        return super().form_valid(f)
    
class editar_publicacion(LoginRequiredMixin, Super_autor_mixin, UpdateView):
    model = Publicacion
    template_name = 'articulos/editar_publicacion.html'
    form_class = PublicacionForm 

    def get_success_url(self):
        return reverse('articulos:lista_publicaciones')

class eliminar_publicacion(LoginRequiredMixin, Super_autor_mixin, DeleteView):
    template_name = 'articulos/eliminar_publicacion.html'
    model = Publicacion

def get_success_url(self):
        return reverse('articulos:lista_publicaciones')