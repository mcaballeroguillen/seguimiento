from django.views.generic import  TemplateView

# Create your views here.
class Paso(TemplateView):
    template_name = 'index.html'

class Paso1(TemplateView):
    template_name = 'home.html'