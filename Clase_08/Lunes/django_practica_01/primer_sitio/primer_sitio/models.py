# Vamos a exportar el modelo usando la libreria de django
from django.db import models

class Products(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)