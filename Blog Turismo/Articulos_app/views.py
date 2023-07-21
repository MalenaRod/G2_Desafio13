from django.shortcuts import render
from django.urls import reverse

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicacion
from .forms import PublicacionForm

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'articulos/lista_publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'articulos/detalle_publicacion.html', {'publicacion': publicacion})

def nueva_publicacion(request):
    if request.method == "POST":
        formulario = PublicacionForm(request.POST)
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
        formulario = PublicacionForm(request.POST, instance=publicacion)
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