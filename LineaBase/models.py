from django.db import models

# Create your models here.
class Temp_Pregunta(models.Model):
    Num= models.IntegerField()
    Tipo= models.CharField(max_length=10)
    Enunciado = models.CharField(max_length=100)
    Opciones = models.CharField(max_length=100)
