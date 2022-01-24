from enum import Flag
from tabnanny import verbose
from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=100, blank=False)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    def __str__(self):
        return self.nombre   

class Venta(models.Model):
    id = models.DateTimeField(primary_key=True)
    numeroArticulo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return str(self.id)    
