from django.db import models

# Create your models here.
class Sitios(models.Model):
    nombre = models.CharField(max_length= 50)
    direccion = models.CharField(max_length=50)
    precio = models.IntegerField(max_length=50)
    calificacion = models.IntegerField(max_length=50)
    serviciosP = models.CharField(max_length=50)

class Usuario(models.Model):
    user = models.CharField(max_length= 50)
    passw = models.CharField(max_length= 50)

class Register(models.Model):
    user1 = models.CharField(max_length= 50)
    pass2 = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)