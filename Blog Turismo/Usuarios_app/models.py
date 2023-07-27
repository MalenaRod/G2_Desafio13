from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    es_usuario = models.BooleanField(default=True)
    es_colaborador = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='imagenes_pefil', blank=True, null=True)

