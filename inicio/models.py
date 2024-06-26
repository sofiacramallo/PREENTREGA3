from django.db import models
class Auto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    anio = models.IntegerField(default=2010)
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField() 
    def __str__(self):
            return f'Soy el alumno {self.nombre} {self.apellido}'
    
class Profesor(models.Model):
   nombre = models.CharField(max_length=30)
   apellido = models.CharField(max_length=30)
   email = models.EmailField()   
   profesion = models.CharField(max_length=30) 

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
