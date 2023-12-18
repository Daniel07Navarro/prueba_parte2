from django.db import models

# Create your models here.
class Pais(models.Model):
    idpais = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5,unique=True)
    nombre = models.CharField(max_length=100)
    poblacion = models.IntegerField()
    estado = models.BooleanField()