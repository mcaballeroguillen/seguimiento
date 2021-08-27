from django.db import models

# Create your models here.
class Temp_Pregunta(models.Model):
    Num= models.IntegerField()
    Tipo= models.CharField(max_length=10)
    Enunciado = models.CharField(max_length=100)
    Opciones = models.CharField(max_length=100)

class Linea_Base(models.Model):
    Usuario = models.CharField(max_length=15)
    Xml = models.FileField(upload_to='LineaBase/Xmls')
    Nombre_proyecto = models.CharField(max_length=50)
    Nombre_encuesta = models.CharField(max_length=50)
