from django.urls import path
from . import views

app_name = 'articulos'

urlpatterns = [
    path('articulos/', views.lista_publicaciones.as_view(), name='lista_publicaciones'),
    path('detalle-articulo/<int:pk>', views.detalle_publicacion.as_view(), name='detalle_publicacion'),
    path('nueva/', views.nueva_publicacion.as_view(), name='nueva_publicacion'),
    path('editar-articulo/<int:pk>', views.editar_publicacion.as_view(), name='editar_publicacion'),
    path('eliminar-articulo/<int:pk>', views.eliminar_publicacion.as_view(success_url='/articulos/articulos'), name='eliminar_publicacion'),
    path('borrar-comentario/<int:pk>', views.BorrarComentario.as_view(), name='borrar-comentario'),
    path('editar-comentario/<int:pk>/', views.EditarComentario.as_view(), name='editar_comentario'),
    path('me-gusta/', views.me_gustaView, name = 'me-gusta'),
]