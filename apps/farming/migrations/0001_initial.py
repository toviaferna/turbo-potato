# Generated by Django 3.2.11 on 2022-07-15 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finance', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acopio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('comprobante', models.CharField(max_length=30, verbose_name='Comprobante')),
                ('peso_bruto', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Peso Bruto')),
                ('peso_tara', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Peso Tara')),
                ('peso_descuento', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Peso Desc.')),
                ('peso_bonificacion', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Peso Bonif.')),
                ('es_transportadora_propia', models.BooleanField(default=False, verbose_name='Es Transportadora Propia?')),
                ('es_vigente', models.BooleanField(default=True, verbose_name='Vigente?')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
            ],
        ),
        migrations.CreateModel(
            name='ActividadAgricola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_documento', models.DateField(verbose_name='Fecha')),
                ('fecha_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Hora Registro')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('es_vigente', models.BooleanField(default=True, verbose_name='Vigente?')),
                ('es_servicio_contratado', models.BooleanField(default=False, verbose_name='Es contratado?')),
                ('cantidad_trabajada', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='HA Trabajada')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.persona', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Actividad agricola',
                'verbose_name_plural': 'Actividades agricolas',
            },
        ),
        migrations.CreateModel(
            name='CalificacionAgricola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Calificación agrícola',
                'verbose_name_plural': 'Calificaciones agrícolas',
            },
        ),
        migrations.CreateModel(
            name='CierreZafra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
            ],
            options={
                'verbose_name': 'Cierre de zafra',
                'verbose_name_plural': 'Cierres de zafras',
            },
        ),
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Descripción')),
                ('dimension_ha', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Dimension Ha')),
                ('ubicacion', models.CharField(max_length=200, verbose_name='Ubicacion')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LiquidacionAgricola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_documento', models.DateField(verbose_name='Fecha')),
                ('fecha_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Hora Registro')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('es_vigente', models.BooleanField(default=True, verbose_name='Vigente?')),
                ('precio_unitario', models.DecimalField(decimal_places=0, max_digits=15, verbose_name='Precio')),
                ('tipo', models.CharField(choices=[('ACOPIOS', 'LIQUIDACION DE ACOPIOS'), ('ACTIVIDADES AGRICOLAS', 'LIQUIDACION DE ACTIVIDADES AGRICOLAS')], max_length=50, verbose_name='Tipo Liquidación')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.persona', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Liquidación agricola',
                'verbose_name_plural': 'Liquidaciones agricolas',
            },
        ),
        migrations.CreateModel(
            name='PlanActividadZafra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
            ],
            options={
                'verbose_name': 'Plan de actividad por zafra',
                'verbose_name_plural': 'Plan de actividades por zafras',
            },
        ),
        migrations.CreateModel(
            name='TipoActividadAgricola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Descripcion')),
                ('es_cosecha', models.BooleanField(verbose_name='es Cosecha')),
                ('es_siembra', models.BooleanField(verbose_name='es Siembra')),
                ('es_resiembra', models.BooleanField(verbose_name='es Resiembra')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tipo de actividad agrícola',
                'verbose_name_plural': 'Tipos de actividades agrícolas',
            },
        ),
        migrations.CreateModel(
            name='TipoMaquinariaAgricola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tipo de maquinaria agrícola',
                'verbose_name_plural': 'Tipos de maquinarias agrícolas',
            },
        ),
        migrations.CreateModel(
            name='Zafra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('anho', models.IntegerField(verbose_name='Anho')),
                ('kg_estimado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Kg Estimado')),
                ('es_zafrinha', models.BooleanField(verbose_name='Es Zafriña?')),
                ('esta_cerrado', models.BooleanField(default=False, verbose_name='Está Cerrado?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.item', verbose_name='Item')),
            ],
        ),
        migrations.CreateModel(
            name='PlanActividadZafraDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actividad', models.DateField(verbose_name='Fecha Act.')),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descripción')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Costo Estimado')),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.finca', verbose_name='Finca')),
                ('plan_actividad_zafra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.planactividadzafra')),
                ('tipo_actividad_agricola', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='farming.tipoactividadagricola', verbose_name='Tipo Actividad Agrícola')),
            ],
        ),
        migrations.AddField(
            model_name='planactividadzafra',
            name='zafra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='farming.zafra', verbose_name='Zafra'),
        ),
        migrations.CreateModel(
            name='MaquinariaAgricola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('es_implemento', models.BooleanField(verbose_name='Es Implemento?')),
                ('admite_implemento', models.BooleanField(verbose_name='Admite Implemento?')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Precio')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tipo_maquinaria_agricola', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.tipomaquinariaagricola', verbose_name='Maquinaria Agrícola Tipo')),
            ],
            options={
                'verbose_name': 'Maquinaria agrícola',
                'verbose_name_plural': 'Maquinarias agrícolas',
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('dimension', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Dimensión HA')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.finca', verbose_name='Finca')),
                ('zafra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.zafra', verbose_name='Zafra')),
            ],
        ),
        migrations.CreateModel(
            name='LiquidacionAgricolaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Cantidad')),
                ('secuencia_origen', models.IntegerField()),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.finca', verbose_name='Finca')),
                ('liquidacion_agricola', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.liquidacionagricola')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.lote', verbose_name='Lote')),
            ],
        ),
        migrations.AddField(
            model_name='liquidacionagricola',
            name='zafra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.zafra', verbose_name='Zafra'),
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_pactado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Precio Pactado')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripción')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.persona', verbose_name='Persona')),
                ('zafra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.zafra', verbose_name='Zafra')),
            ],
        ),
        migrations.CreateModel(
            name='CierreZafraDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ha_cultivada', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='HA Cultivada')),
                ('cantidad_acopio_neto', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='KG Acopiado')),
                ('rendimiento', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Rendimiento')),
                ('costo_total', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Costo Total')),
                ('costo_ha', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Costo HA')),
                ('costo_unitario', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Costo Unit.')),
                ('cierre_zafra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farming.cierrezafra')),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.finca', verbose_name='Finca')),
            ],
        ),
        migrations.AddField(
            model_name='cierrezafra',
            name='zafra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.zafra', verbose_name='Zafra'),
        ),
        migrations.CreateModel(
            name='ActividadAgricolaMaquinariaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ha_trabajada', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Ha Trabajada')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Precio HA')),
                ('actividad_agricola', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.actividadagricola')),
                ('maquinaria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.maquinariaagricola', verbose_name='Maquinaria')),
            ],
        ),
        migrations.CreateModel(
            name='ActividadAgricolaItemDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Costo')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Cantidad')),
                ('porcentaje_impuesto', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='% Impuesto')),
                ('dosis', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Dosis')),
                ('actividad_agricola', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.actividadagricola')),
                ('deposito', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.deposito', verbose_name='Deposito')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.item', verbose_name='Item')),
            ],
        ),
        migrations.AddField(
            model_name='actividadagricola',
            name='finca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.finca', verbose_name='Finca'),
        ),
        migrations.AddField(
            model_name='actividadagricola',
            name='lote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.lote', verbose_name='Lote'),
        ),
        migrations.AddField(
            model_name='actividadagricola',
            name='tipo_actividad_agricola',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.tipoactividadagricola', verbose_name='Tipo Act. Agrícola'),
        ),
        migrations.AddField(
            model_name='actividadagricola',
            name='zafra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.zafra', verbose_name='Zafra'),
        ),
        migrations.CreateModel(
            name='AcopioDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Peso')),
                ('acopio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.acopio')),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.finca', verbose_name='Finca')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.lote', verbose_name='Lote')),
            ],
        ),
        migrations.CreateModel(
            name='AcopioCalificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Grado')),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Porcentaje')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Peso')),
                ('acopio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.acopio')),
                ('calificacion_agricola', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.calificacionagricola', verbose_name='Calif. Agrícola')),
            ],
            options={
                'verbose_name': 'Calificación de acopio',
                'verbose_name_plural': 'Calificaciones de acopios',
            },
        ),
        migrations.AddField(
            model_name='acopio',
            name='camion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.maquinariaagricola', verbose_name='Camión'),
        ),
        migrations.AddField(
            model_name='acopio',
            name='conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.persona', verbose_name='Conductor'),
        ),
        migrations.AddField(
            model_name='acopio',
            name='deposito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.deposito', verbose_name='Depósito'),
        ),
        migrations.AddField(
            model_name='acopio',
            name='zafra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farming.zafra', verbose_name='Zafra'),
        ),
    ]
