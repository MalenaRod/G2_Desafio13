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
        return self.usuario_articulos.count()
    
    def articulos_gustados(self):
        return self.articulos_megusta.count()
    
    def cont_experiencias_aprobadas(self):
        return self.experiencias_set.filter(aprobado_por=self).count()
        
    def experiencias_gustadas(self):
        return self.experiencias_megusta.count()
    
