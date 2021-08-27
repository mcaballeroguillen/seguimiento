from django.urls import path, re_path
from .views import Crear_Linea
app_name = 'lineabase'
urlpatterns = [
    path('crear/',Crear_Linea.as_view(),name="crear"),

]
