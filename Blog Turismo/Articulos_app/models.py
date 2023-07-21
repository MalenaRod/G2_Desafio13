from django.db import models

# Create your models here.

from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_articulos', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)