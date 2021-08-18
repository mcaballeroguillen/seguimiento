from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import  Pregunta_form
from .models import  Temp_Pregunta
# Create your views here.
def nueva_pregunta(request):
    if request.method =='POST':
        p= Temp_Pregunta(
            Num=0,
            Tipo= request.POST['Tipo'],
            Enunciado= request.POST['Enunciado'],
            Opciones= request.POST['Opciones'],
        )
        p.save()
        return HttpResponseRedirect('/thanks/')
    else:
        form = Pregunta_form()
        return  render(request,'nueva_pregunta.html', {'form':form})