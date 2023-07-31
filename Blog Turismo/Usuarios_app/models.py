from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    es_usuario = models.BooleanField(default=True)
    es_colaborador = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='imagenes_pefil', blank=True, null=True)
    sobre_mi = models.TextField(max_length=100, null=True)

    def mensajes_contacto_atendidos(self):
        return self.mensajecontacto_set.filter(atendido_por=self).count()
    
    def articulos_creados(self):
        return self.articulos_app_set.filter(autor=self).count()
    
    def articulos_gustados(self):
        return self.articulos_app_publicacion_megusta_set.filter(usuario_id=self).count()
