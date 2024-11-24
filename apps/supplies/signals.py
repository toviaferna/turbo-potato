from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from apps.inventory.models import Item, ItemMovimiento
from apps.supplies.models import (Compra, CompraDetalle,
                                  NotaCreditoRecibidaDetalle)


@receiver(post_save, sender=Compra)
def signal_compra_guardado(sender, instance, created, **kwargs):
    if created:
        pass
    else:
        if not instance.es_vigente:
            
            item_movimientos = ItemMovimiento.objects.filter(
                tipo_movimiento="CM",
                secuencia_origen=instance.pk
            )
            
            for item_movimiento in item_movimientos:
                item_movimiento.es_vigente = False
                item_movimiento.save()

                # Opcionalmente, reestablecer valores del item
                item = Item.objects.get(pk=item_movimiento.item.pk)
                item.ultimo_costo = item_movimiento.costo
                item.costo = item_movimiento.costo
                item.save()

@receiver(pre_save, sender=CompraDetalle)
def signal_compra_detalle_preguardado(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=CompraDetalle)
def signal_compra_guardado(sender, instance, created, **kwargs):
    if created:
        item_movimiento = ItemMovimiento()
        item_movimiento.item = instance.item
        item_movimiento.deposito = instance.compra.deposito
        item_movimiento.cantidad = instance.cantidad
        item_movimiento.costo = instance.costo
        item_movimiento.precio = 0
        item_movimiento.fecha_documento = instance.compra.fecha_documento
        item_movimiento.secuencia_origen = instance.compra.pk
        item_movimiento.detalle_secuencia_origen = instance.pk
        item_movimiento.es_vigente = True
        item_movimiento.tipo_movimiento = "CM"
        item_movimiento.save()

        item = Item.objects.get(pk=instance.item.pk)
        item.ultimo_costo = instance.costo
        item.costo = instance.costo
        item.save()


            


@receiver(post_save, sender=NotaCreditoRecibidaDetalle)
def signal_nota_credito_recibida_guardado(sender, instance, created, **kwargs):
    if created:
        item_movimiento = ItemMovimiento()
        item_movimiento.item = instance.item
        item_movimiento.deposito = instance.nota_credito_recibida.deposito
        item_movimiento.cantidad = instance.cantidad
        item_movimiento.costo = instance.valor
        item_movimiento.precio = instance.valor
        item_movimiento.fecha_documento = instance.nota_credito_recibida.fecha_documento
        item_movimiento.secuencia_origen = instance.nota_credito_recibida.pk
        item_movimiento.detalle_secuencia_origen = instance.pk
        item_movimiento.es_vigente = True
        item_movimiento.tipo_movimiento = "DC"
        item_movimiento.save()
