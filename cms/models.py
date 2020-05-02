from django.db import models

# Create your models here.

class Pages(models.Model):
    name = models.CharField(max_length=32)
    page = models.TextField()
    
class Contenido(models.Model):
    clave = models.CharField(max_length=64)
    valor = models.TextField()

class Comentario(models.Model):
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField(blank=False)
    fecha = models.DateTimeField('publicado')

