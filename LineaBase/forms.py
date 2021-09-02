from django import  forms
from .models import Temp_Linea_Base

class Linea_Base_form(forms.ModelForm):

    class Meta:
        model = Temp_Linea_Base
        fields = ("Xml","Nombre_proyecto","Nombre_encuesta")



