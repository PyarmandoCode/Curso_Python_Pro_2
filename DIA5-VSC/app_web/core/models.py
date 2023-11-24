from django.db import models

class Productos (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen= models.CharField(max_length=200)

    def __str__(self):
        return self.nombre 


