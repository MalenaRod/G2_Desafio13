from django.db import models
from Usuarios_app.models import Usuario

# Create your models here.
# miapp/models.py


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    pais = models.CharField(max_length=255)
    edad = models.IntegerField()  
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    visto = models.BooleanField( default=False)
    atendido_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
