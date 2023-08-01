from core import views
from django.urls import path, include
from .views import VerContactos, AtenderContacto


urlpatterns = [
	path('', views.indexView, name = 'index'),
    path('usuario/', include('Usuarios_app.urls'), name = 'usuario'),
    path('terminos_condiciones/', views.termViews, name = 'Terminos_Condiciones'),
    path('politica_ptivacidad/', views.politViews, name = 'politica_privacidad'),
    path('articulos/', include('Articulos_app.urls')),
    path('experiencias/', include('Experiencias_app.urls')),
    path('contacto/', views.ContactoCreateView.as_view(), name='contacto'),
    path('cacerca_de/', views.vistaAcerca, name='acerca'),
    path('contacto_exitoso/', views.contacto_exitoso, name='contacto_exitoso'),
    path('mensajes-contacto/', VerContactos.as_view(), name='mensajes_contacto'),
    path('atender-mensaje/<int:pk>/', AtenderContacto.as_view(), name='atender_mensaje'),
] 
