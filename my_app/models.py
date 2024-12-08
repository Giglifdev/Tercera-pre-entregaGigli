from django.db import models


    
class Artistas(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Albums(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Canciones(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo