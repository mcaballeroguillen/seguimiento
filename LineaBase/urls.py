from django.urls import path
from .views import nueva_pregunta
urlpatterns = [
    path('nueva_pregunta/',nueva_pregunta),
]
