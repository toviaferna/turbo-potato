from django.db.models.signals import post_save,pre_save,pre_delete
from django.dispatch import receiver
from apps.inventory.models import AjusteStockDetalle, ItemMovimiento

@receiver(post_save, sender = AjusteStockDetalle)
def signal_ajuste_stock_guardado(sender, instance, created, **kwargs):
    if created:
        item_movimiento = ItemMovimiento()
        item_movimiento.item = instance.item
        item_movimiento.deposito = instance.ajuste_stock.deposito
        item_movimiento.cantidad = instance.cantidad
        item_movimiento.costo = 0
        item_movimiento.precio = 0
        item_movimiento.fecha_documento = instance.ajuste_stock.fecha_documento
        item_movimiento.secuencia_origen = instance.ajuste_stock.pk
        item_movimiento.detalle_secuencia_origen = instance.pk
        item_movimiento.es_vigente = True
        tipo = ''
        if instance.cantidad >= 0:
            tipo = 'AJ+'
        else:
             tipo = 'AJ-'
        item_movimiento.tipo_movimiento = tipo
        item_movimiento.save()