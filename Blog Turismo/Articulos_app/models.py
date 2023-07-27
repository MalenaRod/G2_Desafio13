from Usuarios_app.models import Usuario
from django.db import models
from django.utils.deconstruct import deconstructible
import os

@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # aca obtiene el nombre del archivo
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

def get_upload_path(instance, filename):
    return PathAndRename("imagenes_articulos")(instance, filename)

class Categoria(models.Model):
    cat_nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.cat_nombre

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_articulos', blank=True, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='articulos', null= True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_articulos')

    def delete(self, *args, **kwargs):
        # Eliminar imagen si existe
        if self.imagen:
            self.imagen.delete()
        super().delete(*args, **kwargs)


class Comentario(models.Model):
    texto = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    contenido = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return self.contenido.titulo + '-' + self.autor.first_name