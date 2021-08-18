from django import  forms

class Pregunta_form(forms.Form):
    Tipo= forms.CharField(max_length=10)
    Enunciado = forms.CharField(max_length=100)
    Opciones = forms.CharField(max_length=100)
