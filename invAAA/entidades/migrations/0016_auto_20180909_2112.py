# Generated by Django 2.1.1 on 2018-09-10 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0015_auto_20180909_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_code',
            field=models.CharField(max_length=25, verbose_name='codigo del proyecto'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=200, verbose_name='Nombre proyecto'),
        ),
    ]
