from django.db import models
from Usuarios_app.models import Usuario
from django.utils.deconstruct import deconstructible
import os 

# Create your models here.


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
    return PathAndRename("imagenes_experiencias")(instance, filename)


class Experiencias(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='imagenes_experiencias')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_experiencia')
    megusta= models.ManyToManyField(Usuario, related_name='experiencia_megusta', blank=True)
    aprobado = models.BooleanField( default=False)
    aprobado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)

    def delete(self, *args, **kwargs):
        # Eliminar imagen si existe
        if self.imagen:
            self.imagen.delete()
        super().delete(*args, **kwargs)

    
  #  def cont_experiencias_aprobadas(self):
  #      return self.mensajecontacto_set.filter(atendido_por=self).count()
        
   # def articulos_gustados(self):
   #     return self.articulos_megusta.count()