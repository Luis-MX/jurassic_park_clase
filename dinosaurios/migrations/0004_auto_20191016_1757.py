# Generated by Django 2.2.6 on 2019-10-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurios', '0003_auto_20191015_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='dinosaurio',
            name='imagen',
            field=models.ImageField(upload_to=None, verbose_name='Imágen'),
        ),
    ]