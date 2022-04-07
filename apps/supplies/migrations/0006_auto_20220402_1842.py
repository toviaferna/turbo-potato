# Generated by Django 3.2.11 on 2022-04-02 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0005_notacreditorecibida_notacreditorecibidadetalle_notadebitorecibida_notadebitorecibidadetalle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuotacompra',
            options={'verbose_name': 'Cuota de compra', 'verbose_name_plural': 'Cuotas de compras'},
        ),
        migrations.AlterModelOptions(
            name='notacreditorecibida',
            options={'verbose_name': 'Nota de crédito recibida', 'verbose_name_plural': 'Notas de crédito recibidas'},
        ),
        migrations.AlterModelOptions(
            name='notadebitorecibida',
            options={'verbose_name': 'Nota de débito recibida', 'verbose_name_plural': 'Notas de débito recibidas'},
        ),
        migrations.AlterModelOptions(
            name='ordencompra',
            options={'verbose_name': 'Orden de compra', 'verbose_name_plural': 'Ordenes de compras'},
        ),
        migrations.AlterModelOptions(
            name='pedidocompra',
            options={'verbose_name': 'Pedido de compra', 'verbose_name_plural': 'Pedidos de compras'},
        ),
    ]