# Generated by Django 2.1.1 on 2018-09-10 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0008_auto_20180909_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_code',
            field=models.IntegerField(verbose_name='Codigo empleado'),
        ),
    ]