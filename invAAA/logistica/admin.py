from django.contrib import admin
from .models import Inventory,EquipmentInv


# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['headquarter_name','iventory_date','department_name','created','updated',] 
    search_fields = ['headquarter_name__headquarter_name','department_name__department_name','id','iventory_date']
    list_filter = ['headquarter_name']

class EquipmentInvAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['cod_amerika','t_name','employee_name'] 
    search_fields = ['cod_amerika','t_name__type_name','serial','employee_name__employee_name']
    list_filter = ['t_name']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "inventory":
            kwargs["queryset"] = Inventory.objects.filter(status_open=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Inventory,InventoryAdmin)
admin.site.register(EquipmentInv,EquipmentInvAdmin)

