from django.db import models

# Create your models here.

class Group(models.Model):
    group_code = models.CharField(max_length=3,verbose_name='Codigo')
    group_name = models.CharField(max_length=25,verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de ultima edición")

    class Meta:
        verbose_name = "grupo"
        verbose_name_plural = "grupos"
        ordering = ["-created"]


    def __str__(self):
        return self.group_code


class Sub_Group(models.Model):
    subgroup_code = models.CharField(max_length=3,verbose_name='Codigo')
    subgroup_name = models.CharField(max_length=25,verbose_name='Nombre')
    # group = models.ForeignKey(Group,on_delete=models.PROTECT,verbose_name='Grupo')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de ultima edición")

    class Meta:
        verbose_name = "subgrupo"
        verbose_name_plural = "subgrupos"
        ordering = ["-created"]


    def __str__(self):
        return self.subgroup_code

# class Headquarter(models.Model):
#     headquarter_name = models.CharField(max_length=25, verbose_name="Nombre")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

#     class Meta:
#         verbose_name = "sede"
#         verbose_name_plural = "sedes"
#         ordering = ["-created"]

#     def __str__(self):
#         return self.headquarter_name

# class Department(models.Model):
#     department_name = models.CharField(max_length=25, verbose_name="Nombre")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

#     class Meta:
#         verbose_name = "departamento"
#         verbose_name_plural = "departamentos"
#         ordering = ["-created"]

#     def __str__(self):
#         return self.department_name

class Type(models.Model):
    type_name = models.CharField(max_length=25, verbose_name="tipo de equipo")
    # subgroup_t = models.ForeignKey(Sub_Group,on_delete=models.PROTECT,verbose_name='subgrupo')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    

    class Meta:
        verbose_name = "tipo"
        verbose_name_plural = "tipos"
        ordering = ["-created"]

    def __str__(self):
        return self.type_name
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=25, verbose_name="marca")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        ordering = ["-created"]

    def __str__(self):
        return self.brand_name


# class Employee(models.Model):
#     employee_code = models.IntegerField( verbose_name="Codigo")    
#     employee_name = models.CharField(max_length=25, verbose_name="Nombre")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

#     class Meta:
#         verbose_name = "empleado"
#         verbose_name_plural = "empleados"
#         ordering = ["-created"]

#     def __str__(self):
#         return self.employee_name

class Characteristic(models.Model):
    characteristic = models.CharField(max_length=25, verbose_name="Nombre")
    # tipo = models.ForeignKey(Type,on_delete=models.PROTECT,verbose_name='tipo')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "caracterica"
        verbose_name_plural = "caracteristica"
        ordering = ["-created"]

    def __str__(self):
        return self.characteristic 

class Modelo(models.Model):
    modelo_name = models.CharField(max_length=25, verbose_name="Nombre")
    # brand = models.ForeignKey(Brand,on_delete=models.PROTECT,verbose_name='Marca')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelos"
        ordering = ["-created"]

    def __str__(self):
        return self.modelo_name 

class Status(models.Model):
    status_code = models.CharField(max_length=25, verbose_name="Codigo")
    status_name = models.CharField(max_length=25, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "status"
        verbose_name_plural = "status"
        ordering = ["-created"]

    def __str__(self):
        return self.status_code 