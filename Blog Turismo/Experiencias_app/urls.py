from django.urls import path
from . import views

app_name = 'experiencias'

urlpatterns = [
    path('experiencias/', views.ListaExperiencias.as_view(), name='experiencias'),
    path('experiencias_Noaprobadas/', views.ListaExperiencias.as_view(template_name='experiencias/experiencias_noaprob.html'), name='experiencias_Noaprobadas'),
    path('aprobar_experiencias/<int:pk>/', views.AprobarExperiencia.as_view(), name='aprobar_experiencias'),
    path('crear_experiencia/', views.NuevaExperiencia.as_view(), name='crear_experiencia'),
    path('experiencia_creada/', views.experiencia_creada, name='experiencia_creada'),
    path('eliminar_experiencia/<int:pk>/', views.EliminarExperiencia.as_view(), name= 'eliminar_experiencia'),
    ]
    
