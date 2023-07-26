from django.db import models
from Usuarios_app.models import Usuario

# Create your models here.

from django.db import models

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

'''    class Meta:
        ordering = ['fecha_publicacion']

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()
    '''
class Comentario(models.Model):
    texto = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return self.post.titulo + '-' + self.autor.first_name