# Generated by Django 3.2.11 on 2022-03-06 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('supplies', '0002_auto_20220305_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='item',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tipo_impuesto',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tipo_item',
        ),
        migrations.AlterField(
            model_name='compra',
            name='deposito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.deposito', verbose_name='Deposito'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.item', verbose_name='Item'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Deposito',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.DeleteModel(
            name='TipoImpuesto',
        ),
        migrations.DeleteModel(
            name='TipoItem',
        ),
    ]
