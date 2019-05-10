from django.db import models

# Create your models here.
class User(models.Model):
    usuar = models.CharField(max_length=25)
    passw = models.CharField(max_length=50)
