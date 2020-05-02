from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contenido

def get_content(request, llave):
    contenido = Contenido.objects.get(clave=llave)
    return HttpResponse(contenido.valor)
