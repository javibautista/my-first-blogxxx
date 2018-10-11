from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
         return self.title
"""
El sistema llevará un registro de personas, de las cuales se consignará: Apellido y nombre, DNI, edad, fecha de nacimiento y fecha de alta.
La información se almacenará en una base de datos PostgreSQL.
La página inicial deberá contener una barra que permita hacer búsquedas por DNI.
El còdigo se alojará en github.
"""

class Persona(models.Model):
    persona = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    apellido = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    dni = models.CharField(max_length=200, default='')
    edad = models.CharField(max_length=200)
    fech_nac = models.DateTimeField(blank=True, null=True)
    alta = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
         return self.title
