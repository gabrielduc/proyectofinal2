from django.db import models

# Create your models here.



class Profesional(models.Model):
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    especialidad = models.CharField(max_length=50)  # Se puede convertir en ForeignKey si se tiene una tabla de especialidades

    def __str__(self) :
        return self.nombre
    
class ClienteGimnasio(models.Model):
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    entrenador = models.ForeignKey('gymapp.Profesional', on_delete=models.CASCADE, related_name='alumnos')

    def __str__(self) :
        return self.nombre

class Servicio(models.Model):
    TIPO_CHOICES = (
        ('normal', 'Normal'),
        ('premium', 'Premium'),
        ('kinesiologo', 'Kinesiólogo'),
        ('nutricionista', 'Nutricionista'),
    )
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)

    def __str__(self) :
        return self.tipo
