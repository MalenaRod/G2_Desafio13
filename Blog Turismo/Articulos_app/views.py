from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicacion, Categoria
from .forms import PublicacionForm, ComentarioForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


#cambio de funcion a clase
'''def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'articulos/lista_publicaciones.html', {'publicaciones': publicaciones})'''

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
        orden = self.request.GET.get('orderby')
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



# Cambio de funcion a clase la view del detalle de publicación

'''def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'articulos/detalle_publicacion.html', {'publicacion': publicacion})'''

class detalle_publicacion(DetailView):
    model = Publicacion
    template_name = "articulos/detalle_publicacion.html"
    context_object_name = 'articulo'

    #metodo para crear un metodo post en el detalle de publicacion
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comentario'] = ComentarioForm()
        return context
    
    


def nueva_publicacion(request):
    if request.method == "POST":
        formulario = PublicacionForm(request.POST, request.FILES)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.save()
            return redirect('articulos/../../../articulos', pk=publicacion.pk)

     #return redirect('articulos/detalle_publicacion', pk=publicacion.pk)
     #return reverse('articulos:lista_publicaciones')
    
    else:
        formulario = PublicacionForm()
    return render(request, 'articulos/nueva_publicacion.html', {'formulario': formulario})

def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        formulario = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        formulario = PublicacionForm(instance=publicacion)
    return render(request, 'articulos/editar_publicacion.html', {'formulario': formulario})

def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    publicacion.delete()
    return redirect('lista_publicaciones')