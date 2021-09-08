from django.urls import path, re_path
from .views import Subir_Linea, Drive_manage, Crear_Encuesta
app_name = 'lineabase'
urlpatterns = [
    path('subir/', Subir_Linea.as_view(), name="subir"),
    path('drive/',Drive_manage.as_view(), name='drive'),
    path('crear_1/',Crear_Encuesta.as_view(),name='crear'),

]
