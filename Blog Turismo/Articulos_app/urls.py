from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.lista_publicaciones, name='lista_publicaciones'),
    path('publicacion/<int:pk>/', views.detalle_publicacion.as_view(), name='detalle_publicacion'),
    path('publicacion/nueva/', views.nueva_publicacion, name='nueva_publicacion'),
    path('publicacion/<int:pk>/editar/', views.editar_publicacion, name='editar_publicacion'),
    path('publicacion/<int:pk>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
]