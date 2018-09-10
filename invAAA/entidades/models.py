from django.db import models

# Create your models here.

class Project(models.Model):
    project_code = models.CharField(max_length=25,verbose_name="nombre del proyecto")
    project_name = models.CharField(max_length=200, verbose_name="codigo proyecto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de ultima edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]


    def __str__(self):
        return self.project_name
    

class Headquarter(models.Model):
    headquarter_name = models.CharField(max_length=25, verbose_name="Nombre de la sede")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "sede"
        verbose_name_plural = "sedes"
        ordering = ["-created"]

    def __str__(self):
        return self.headquarter_name

class Department(models.Model):
    department_name = models.CharField(max_length=25, verbose_name="Nombre del departamento")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"
        ordering = ["-created"]

    def __str__(self):
        return self.department_name

class Type(models.Model):
    type_name = models.CharField(max_length=25, verbose_name="tipo de equipo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tipo"
        verbose_name_plural = "tipos"
        ordering = ["-created"]

    def __str__(self):
        return self.type_name
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=25, verbose_name="marca del equipo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        ordering = ["-created"]

    def __str__(self):
        return self.brand_name


class Employee(models.Model):
    employee_code = models.IntegerField( verbose_name="Codigo empleado")    
    employee_name = models.CharField(max_length=25, verbose_name="Nombre empleado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"
        ordering = ["-created"]

    def __str__(self):
        return self.employee_name