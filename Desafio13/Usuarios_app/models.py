from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class Usuario(AbstractBaseUser):
    es_usuario = models.BooleanField(default=True),
    es_colaborador = models.BooleanField(default=False),
    es_admin = models.BooleanField(default=False),
