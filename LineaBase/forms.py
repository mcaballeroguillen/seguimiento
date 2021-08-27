from django import  forms
from .models import Linea_Base

class Linea_Base(forms.ModelForm):
    class Meta:
        model = Linea_Base
        fields = ("Xml","Nombre_proyecto","Nombre_encuesta")

