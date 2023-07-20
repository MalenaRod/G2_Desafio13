from core import views
from django.urls import path, include

urlpatterns = [
	path('index/', views.indexView, name = 'index'),
#    path('usuario/', include('usuarios_app.urls'), name = 'usuario'),
] 
