# Generated by Django 3.2.11 on 2022-04-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_tipoimpuesto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipoimpuesto',
            options={'verbose_name_plural': 'Tipos de impuestos'},
        ),
    ]