# Generated by Django 3.2.11 on 2022-03-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoImpuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Descripcion')),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='% Impuesto')),
                ('es_iva', models.BooleanField(max_length=200, verbose_name='es IVA?')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
