# Generated by Django 3.2.11 on 2022-03-06 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.departamento', verbose_name='Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.distrito', verbose_name='Distrito')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abreviatura', models.CharField(max_length=200, unique=True, verbose_name='Descripcion')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=200, verbose_name='Razon Social')),
                ('documento', models.CharField(max_length=40, verbose_name='Documento')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion')),
                ('celular', models.CharField(blank=True, max_length=60, null=True, verbose_name='Celular / Telefono')),
                ('es_cliente', models.BooleanField(default=False, help_text='La persona será tratada como un cliente', verbose_name='Es Cliente?')),
                ('es_proveedor', models.BooleanField(default=False, help_text='La persona será tratada como un proveedor', verbose_name='Es Proveedor?')),
                ('es_empleado', models.BooleanField(default=False, help_text='La persona será tratada como un empleado de la empresa', verbose_name='Es Empleado?')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.localidad', verbose_name='Localidad')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.pais', verbose_name='Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Descripcion')),
                ('es_banco', models.BooleanField(default=False, verbose_name='Es Banco?')),
                ('nro_cuenta', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nro Cuenta')),
                ('banco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finance.banco', verbose_name='Banco')),
            ],
        ),
    ]