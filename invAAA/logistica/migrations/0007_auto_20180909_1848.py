# Generated by Django 2.1.1 on 2018-09-10 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0006_inventory_department_nam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='department_nam',
            new_name='department_name',
        ),
    ]