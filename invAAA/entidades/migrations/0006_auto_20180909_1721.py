# Generated by Django 2.1.1 on 2018-09-09 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0005_auto_20180909_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=25, verbose_name='marca del equipo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.CharField(max_length=25, verbose_name='tipo de equipo'),
        ),
    ]