from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import  Linea_Base
from pydrive.auth import  GoogleAuth
from pydrive.drive import GoogleDrive

# Create your views here.

class Crear_Linea(TemplateView):


    def post(self,request, *args, **kwargs):
        form = Linea_Base(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form.cleaned_data.update(
                Usuario=request.user.username
            )
            return redirect("")

    def get(self, request, *args, **kwargs):
        form = Linea_Base


        return  render(request, "Lineas_Base/Crear_Linea_Base.html",{'formulario':form})


class Drive_manage (TemplateView):

    def __init__(self):
        self.drive = "s"
    def autenticar(self):
            ga = GoogleAuth()
            ga.LocalWebserverAuth()
            self.drive= ga
    def crear_carpeta(self):
            dr = GoogleDrive(self.drive)
            folder = dr.CreateFile({'title': 'My Awesome Folder 123', "mimeType": "application/vnd.google-apps.folder"})
            folder.Upload()
    def get(self, request, *args, **kwargs):
        self.autenticar()
        self.crear_carpeta()

        return redirect("lineabase:crear")


