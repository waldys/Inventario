from django.db import models

# Create your models here.


class Projecto(models.Model):
    projecto_code = models.CharField(max_length=3,verbose_name="Codigo ")
    projecto_name = models.CharField(max_length=25, verbose_name="Nombre ")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de ultima edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]


    def __str__(self):
        return self.projecto_code


class Departmento(models.Model):
    departmento_name = models.CharField(max_length=25, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"
        ordering = ["-created"]

    def __str__(self):
        return self.departmento_name

class Sede(models.Model):
    sede_name = models.CharField(max_length=25, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "sede"
        verbose_name_plural = "sedes"
        ordering = ["-created"]

    def __str__(self):
        return self.sede_name