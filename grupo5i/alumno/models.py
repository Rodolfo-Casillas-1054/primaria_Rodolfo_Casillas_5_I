from django.db import models

# Create your models here.

class Alumno(models.Model):
    apaterno = models.CharField(max_length=50, verbose_name= "Apellido Paterno jajajaja")
    amaterno = models.CharField(max_length=50, varbose_name= "Apellido Materno")
    nombre = models.CharField(max_length=100, verbose_name="Nombres (s)")
    fecha_de_nacimiento = models.CharField(verbose_name="Fecha de Nacimiento", null=False, blank=False)
    fecha_de_ingreso = models.CharField(verbose_name="Fecha de Ingreso", null=False, blank=False)