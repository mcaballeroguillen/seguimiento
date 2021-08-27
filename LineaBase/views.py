from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import  Linea_Base

# Create your views here.

class Crear_Linea(TemplateView):


    def post(self,request, *args, **kwargs):
        form = Linea_Base(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("")

    def get(self, request, *args, **kwargs):
        form = Linea_Base
        return  render(request, "Lineas_Base/Crear_Linea_Base.html",{'formulario':form})


