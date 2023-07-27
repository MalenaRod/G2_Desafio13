from core import views
from django.urls import path, include


urlpatterns = [
	path('', views.indexView, name = 'index'),
    path('usuario/', include('Usuarios_app.urls'), name = 'usuario'),
    path('articulos/', include('Articulos_app.urls')),
    path('contacto/', views.ContactoCreateView.as_view(), name='contacto'),
    path('cacerca_de/', views.vistaAcerca, name='acerca'),
    path('contacto_exitoso/', views.contacto_exitoso, name='contacto_exitoso')
] 
