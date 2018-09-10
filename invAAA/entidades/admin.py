from django.contrib import admin
from .models import Project,Headquarter,Department,Type,Brand,Employee


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['id','project_code','project_name','created','updated',] 

class HeadquarterAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['id','headquarter_name','created','updated',] 

class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['id','department_name','created','updated',] 

class TypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['id','type_name','created','updated',] 

class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['id','employee_code','employee_name','created','updated',] 


class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['id','brand_name','created','updated',] 

admin.site.register(Project, ProjectAdmin)  
admin.site.register(Headquarter,HeadquarterAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Employee,EmployeeAdmin)


