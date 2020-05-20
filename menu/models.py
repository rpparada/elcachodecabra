from django.db import models
from elcachodecabra.parametros import parECC

# Create your models here.

class promociones(models.Model):

    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre

class pizza(models.Model):

    nombre = models.CharField(max_length=200)
    precio_fam = models.IntegerField()
    precio_ind = models.IntegerField()
    ingredientes = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
