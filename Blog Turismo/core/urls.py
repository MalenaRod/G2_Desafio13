from core import views
from django.urls import path, include


urlpatterns = [
	path('', views.indexView, name = 'index'),
    path('usuario/', include('Usuarios_app.urls'), name = 'usuario'),
    path('articulos/', include('Articulos_app.urls')),
    path('contacto/', views.vistaContactenos, name='contacto'),
    path('cacerca_de/', views.vistaAcerca, name='acerca'),
] 
