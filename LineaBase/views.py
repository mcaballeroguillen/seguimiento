from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import  Linea_Base_form
from pydrive.auth import  GoogleAuth
from pydrive.drive import GoogleDrive
from .models import Temp_Linea_Base, Linea_Base
from .utils.xform_tools import formversion_pyxform

# Create your views here.

class Subir_Linea(TemplateView):


    def post(self,request, *args, **kwargs):
        form = Linea_Base_form(request.POST, request.FILES)
        if form.is_valid():
            Temp_Linea_Base.objects.all().delete()
            Linea_Base.objects.all().delete()

            form.save()
            return redirect("lineabase:drive")

    def get(self, request, *args, **kwargs):
        form = Linea_Base_form


        return  render(request, "Lineas_Base/Crear_Linea_Base.html",{'formulario':form})


class Drive_manage (TemplateView):

    def __init__(self):
        self.drive = "s"
    def autenticar(self):
            ga = GoogleAuth()
            #ga.LocalWebserverAuth()
            ga.LoadCredentialsFile("mycreds.txt")
            self.drive= ga

    def crear_carpeta(self):
            dr = GoogleDrive(self.drive)
            datos = Temp_Linea_Base.objects.get(Usuario= "user0")
            Proyecto = datos.Nombre_proyecto
            folder = dr.CreateFile({'title': Proyecto, "mimeType": "application/vnd.google-apps.folder"})
            folder.Upload()
            datos.Folder_id = folder['id']
            datos.Usuario = self.request.user.username
            datos.save()

    def crear_archivo_excel(self):
        dr = GoogleDrive(self.drive)
        datos = Temp_Linea_Base.objects.get(Usuario=self.request.user.username)
        nombre_e = datos.Nombre_encuesta
        folder = datos.Folder_id
        sheel = dr.CreateFile({
            'title': nombre_e,
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parents': [{'id':folder}]

        })
        sheel.Upload()
        permiso = sheel.InsertPermission({
            'type': 'anyone',
            'value': 'anyone',
            'role': 'writer'
        })
        link = sheel['alternateLink']
        id = sheel['id']
        datos.File_Id=id
        datos.File_url=link
        datos.save()

    def preparar_archivo(self):
        datos = Temp_Linea_Base.objects.get(Usuario=self.request.user.username)
        Nombre_E = datos.Nombre_encuesta
        archivo_name= "LineaBase/Xmls/"+Nombre_E + ".xml"
        name_orginal = datos.filename()
        archivo_orginal = "LineaBase/Xmls/"+ name_orginal

        archivo = open(archivo_name, 'w')
        f = open(archivo_orginal,'r')
        lineas = f.readlines()
        for linea in lineas:
            l = str(linea)
            if "</instance>" in l:
                archivo.write(l)
                nueva_l = "<submission method=\"form-data-post\" action=\""+ datos.File_url+ "\"/\n>"
                archivo.write(nueva_l)
            else:
                archivo.write(l)
        archivo.close()


    def subir_archivo(self):
        datos = Temp_Linea_Base.objects.get(Usuario=self.request.user.username)
        Nombre_E = datos.Nombre_encuesta
        archivo_name = "LineaBase/Xmls/" + Nombre_E + ".xml"
        Fo_if = datos.Folder_id
        dr = GoogleDrive(self.drive)
        A = dr.CreateFile()
        A.SetContentFile(archivo_name)
        A['title']= Nombre_E + ".xml"
        A['parents'] = [{"kind": "drive#parentReference", "id": Fo_if}]
        A.Upload()
        datos.File_Id = A['id']



    def get(self, request, *args, **kwargs):
        self.autenticar()
        self.crear_carpeta()
        self.crear_archivo_excel()
        self.preparar_archivo()
        self.subir_archivo()


        return redirect("subir")



class Crear_Encuesta(TemplateView):

    def get(self, request, *args, **kwargs):
        pyxform_survey = formversion_pyxform({
            'survey': [
                {'type': 'text',
                 'name': 'q1',
                 'label': 'text question'},
                {'type': 'select_one colors',
                 'name': 'color',
                 'label': 'color'}
            ],
            'choices': [
                {'list_name': 'colors', 'value': 'red', 'label': 'Red'},
                {'list_name': 'colors', 'value': 'blue', 'label': 'Blue'},
            ],
            'settings': {'id_string': 'simple',
                         'title': 'simple example xform',
                         'name': 'data'}
        })

        print(
            pyxform_survey.to_xml()
        )

        file = "LineaBase/Xmls/"+"prueba"+".xml"
        f = open(file,'w')
        f.write(pyxform_survey.to_xml())
