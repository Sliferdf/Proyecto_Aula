from django.db import models

# Create your models here.
class Sitios(models.Model):
    nombre = models.CharField(max_length= 50)
    direccion = models.CharField(max_length=50)
    precio = models.IntegerField(max_length=50)
    calificacion = models.IntegerField(max_length=50)
    serviciosP = models.CharField(max_length=50)
