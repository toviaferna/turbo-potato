# Generated by Django 3.2.11 on 2023-10-30 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45, verbose_name='Descripcion')),
                ('simbolo', models.CharField(max_length=15, verbose_name='Abreviatura')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='unidad_medida',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.unidadmedida', verbose_name='Unidad de medida'),
        ),
    ]
