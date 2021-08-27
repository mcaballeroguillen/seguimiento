from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import  Pregunta_form
from .models import  Temp_Pregunta
# Create your views here.

class Crear_Linea(TemplateView):
    template_name = "Lineas_Base/Crear_Linea_Base.html"
