# Generated by Django 2.1.1 on 2018-09-10 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0010_auto_20180909_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='p',
            field=models.CharField(default=1, max_length=45, verbose_name='prrr'),
            preserve_default=False,
        ),
    ]