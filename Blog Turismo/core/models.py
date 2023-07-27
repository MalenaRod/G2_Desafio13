from django.db import models

# Create your models here.
# miapp/models.py


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    pais = models.CharField(max_length=255)
    edad = models.IntegerField()  
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
