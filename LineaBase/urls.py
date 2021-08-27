from django.urls import path, re_path
from .views import Crear_Linea, Drive_manage
app_name = 'lineabase'
urlpatterns = [
    path('crear/',Crear_Linea.as_view(),name="crear"),
    path('drive/',Drive_manage.as_view(), name='drive'),

]
