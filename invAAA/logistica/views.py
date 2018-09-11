from django.shortcuts import render
import pdfkit
from django_pdfkit import PDFView
from .models import EquipmentInv,Inventory

# Create your views here.


class Inventario(PDFView):
    
   
    template_name = "logistica/inventario.html"

    def  get_context_data(self, **kwargs):
        id_inventario =str(self.request.GET.get('id'))
        inline=True
        context = super().get_context_data(**kwargs)
        equip = Inventory.objects.get(pk=id_inventario)

        context = {'equip':equip}

        return context




