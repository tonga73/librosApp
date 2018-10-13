from django.db import models

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100, blank=False, default='')
    foto = models.ImageField(blank=True)


class Cuento(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='cuentos')
    titulo = models.CharField(max_length=100, blank=False, default='')
    texto = models.TextField()

