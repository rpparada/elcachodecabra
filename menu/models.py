from django.db import models
from elcachodecabra.parametros import parECC

# Create your models here.
class menu(models.Model):

    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    ingredientes = models.TextField(blank=True)
    tamaño = models.CharField(max_length=2, choices=parECC['tamanoPlato'], blank=True)

    def __str__(self):
        return self.nombre+' - '+self.tamaño

class promociones(models.Model):

    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre
