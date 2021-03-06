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
            name='AperturaCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('fecha_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Apertura')),
                ('esta_cerrado', models.BooleanField(default=False, verbose_name='Esta Cerrado?')),
                ('monto_inicio', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Monto Inicial')),
                ('fecha_hora_cierre', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha Cierre')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.persona', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Apertura de caja',
                'verbose_name_plural': 'Apertura de cajas',
            },
        ),
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_documento', models.DateField(verbose_name='Fecha')),
                ('fecha_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Hora Registro')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('es_vigente', models.BooleanField(default=True, verbose_name='Vigente?')),
                ('monto_a_saldar', models.DecimalField(decimal_places=0, max_digits=15, verbose_name='Monto A Saldar')),
                ('comprobante', models.CharField(max_length=15, verbose_name='Comprobante')),
                ('apertura_caja', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.aperturacaja', verbose_name='Apertura Caja')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente', to='finance.persona', verbose_name='Cliente')),
                ('cobrador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cobrador', to='finance.persona', verbose_name='Cobrador')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.cuenta', verbose_name='Cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='NotaCreditoEmitida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_documento', models.DateField(verbose_name='Fecha Documento')),
                ('fecha_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Hora Registro')),
                ('comprobante', models.CharField(max_length=15, verbose_name='Comprobante')),
                ('timbrado', models.CharField(max_length=8, verbose_name='Timbrado')),
                ('es_credito', models.BooleanField(default=False, verbose_name='Es Crédito?')),
                ('es_vigente', models.BooleanField(default=True, verbose_name='Vigente?')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.persona', verbose_name='Cliente')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.cuenta', verbose_name='Cuenta')),
                ('deposito', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.deposito', verbose_name='Deposito')),
            ],
            options={
                'verbose_name': 'Nota de crédito emitida',
                'verbose_name_plural': 'Notas de crédito emitidas',
            },
        ),
        migrations.CreateModel(
            name='NotaDebitoEmitida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_documento', models.DateField(verbose_name='Fecha Documento')),
                ('fecha_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Hora Registro')),
                ('comprobante', models.CharField(max_length=15, verbose_name='Comprobante')),
                ('timbrado', models.CharField(max_length=8, verbose_name='Timbrado')),
                ('es_credito', models.BooleanField(default=False, verbose_name='Es Crédito?')),
                ('es_vigente', models.BooleanField(default=True, verbose_name='Vigente?')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.persona', verbose_name='Cliente')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.cuenta', verbose_name='Cuenta')),
                ('deposito', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.deposito', verbose_name='Deposito')),
            ],
            options={
                'verbose_name': 'Nota de débito emitida',
                'verbose_name_plural': 'Notas de débito emitidas',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_documento', models.DateField(verbose_name='Fecha')),
                ('fecha_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Hora Registro')),
                ('comprobante', models.CharField(max_length=15, verbose_name='Comprobante')),
                ('timbrado', models.CharField(max_length=8, verbose_name='Timbrado')),
                ('es_credito', models.BooleanField(default=True, verbose_name='Es Crédito?')),
                ('es_vigente', models.BooleanField(default=True, verbose_name='Vigente?')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('apertura_caja', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.aperturacaja', verbose_name='AperturaCaja')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.persona', verbose_name='Cliente')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.cuenta', verbose_name='Cuenta')),
                ('deposito', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.deposito', verbose_name='Deposito')),
            ],
        ),
        migrations.CreateModel(
            name='VentaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Cantidad')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Costo')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Precio')),
                ('porcentaje_impuesto', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='% Impuesto')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.item', verbose_name='Item')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.venta')),
            ],
        ),
        migrations.CreateModel(
            name='TransferenciaCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Monto a Transferir')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('es_vigente', models.BooleanField(default=True, verbose_name='Vigente?')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('comprobante', models.CharField(default='', max_length=15, verbose_name='Comprobante')),
                ('apertura_caja', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.aperturacaja', verbose_name='Cuenta Entrada')),
                ('cuenta_entrada', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entrada', to='finance.cuenta', verbose_name='Cuenta Entrada')),
                ('cuenta_salida', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salida', to='finance.cuenta', verbose_name='Cuenta Salida')),
            ],
            options={
                'verbose_name': 'Transferencia de cuenta',
                'verbose_name_plural': 'Transferencias de cuentas',
            },
        ),
        migrations.CreateModel(
            name='NotaDebitoEmitidaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Cantidad')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Costo/Descuento')),
                ('porcentaje_impuesto', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='% Impuesto')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.item', verbose_name='Item')),
                ('nota_debito_emitida', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.notadebitoemitida')),
            ],
        ),
        migrations.AddField(
            model_name='notadebitoemitida',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.venta', verbose_name='Venta'),
        ),
        migrations.CreateModel(
            name='NotaCreditoEmitidaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Cantidad')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Costo/Descuento')),
                ('es_devolucion', models.BooleanField(default=False, verbose_name='Es Devolución?')),
                ('porcentaje_impuesto', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='% Impuesto')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.item', verbose_name='Item')),
                ('nota_credito_emitida', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.notacreditoemitida')),
            ],
        ),
        migrations.AddField(
            model_name='notacreditoemitida',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.venta', verbose_name='Venta'),
        ),
        migrations.CreateModel(
            name='CuotaVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha Vencimiento')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Monto')),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Saldo')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.venta')),
            ],
            options={
                'verbose_name': 'Cuota de venta',
                'verbose_name_plural': 'Cuotas de ventas',
            },
        ),
        migrations.CreateModel(
            name='CobroMedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15, verbose_name='N°')),
                ('comprobante', models.CharField(max_length=15, verbose_name='Comprobante')),
                ('monto', models.DecimalField(decimal_places=0, max_digits=15, verbose_name='Monto')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('medio_cobro', models.CharField(choices=[('CHEQUE DIF', 'CHEQUE DIFERIDO'), ('CHEQUE DIA', 'CHEQUE AL DIA'), ('EFECTIVO', 'EFECTIVO'), ('TRANSFERENCIA', 'TRANSFERENCIA BANCARIA')], max_length=50, verbose_name='Medio Cobro')),
                ('cobro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.cobro')),
            ],
            options={
                'verbose_name': 'Medio de cobro',
                'verbose_name_plural': 'Medios de cobros',
            },
        ),
        migrations.CreateModel(
            name='CobroDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelacion', models.DecimalField(decimal_places=0, max_digits=15, verbose_name='Cancelacion')),
                ('cobro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.cobro')),
                ('cuota_venta', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sales.cuotaventa', verbose_name='Cuota Venta')),
            ],
        ),
        migrations.CreateModel(
            name='Arqueo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observación')),
                ('fecha_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Hora Registro')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Monto Retirado')),
                ('apertura_caja', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.aperturacaja', verbose_name='Apertura Caja')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.persona', verbose_name='Empleado')),
            ],
        ),
    ]
