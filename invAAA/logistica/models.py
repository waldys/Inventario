from django.db import models
from entidades.models import *

# Create your models here.
headquarter = Headquarter()
department = Department
class Inventory(models.Model):
    iventory_date = models.DateField(verbose_name="Fecha")
    status_open = models.BooleanField(default=True, verbose_name="Activar inventario")
    headquarter_name = models.ForeignKey(headquarter,on_delete=models.CASCADE,verbose_name="Nombre de la sede")
    department_name = models.ForeignKey(department,on_delete=models.CASCADE,verbose_name='nombre del departaamento')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de ultima edición")

    class Meta:
        verbose_name = "inventario"
        verbose_name_plural = "inventarios"
        ordering = ["-created"]


    def __str__(self):
        return ("Inventario de {} para la fecha {} ".format(self.headquarter_name,self.iventory_date))

class EquipmentInv(models.Model):
    inventarios = Inventory.objects.filter(status_open="True")
    STATUS = (
        ('A', 'Activo'),
        ('R', 'Reparacion'),
        ('D', 'Danado'),
    )

    cod_amerika = models.IntegerField(verbose_name="Codigo de Amerika" )
    serial = models.CharField(max_length=30,verbose_name="Numero de serie",blank=True)
    status = models.CharField(max_length=1, choices=STATUS)
    observation =models.TextField(verbose_name="Descripción",blank=True)
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE,verbose_name='Inventario')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de ultima edición")
    project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='proyecto')
    t_name = models.ForeignKey(Type,on_delete=models.CASCADE,verbose_name='tipo')
    brand_name =models.ForeignKey(Brand,on_delete=models.CASCADE,verbose_name='marca')
    employee_name = models.ForeignKey(Employee,on_delete=models.CASCADE,verbose_name='empleado')

    class Meta:
        verbose_name = "equipoInv"
        verbose_name_plural = "equiposInv"
        ordering = ["-created"]

    def __str__(self):
        return "{} cod AMK: {}".format(self.t_name,self.cod_amerika)