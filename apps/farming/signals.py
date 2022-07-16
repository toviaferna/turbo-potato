from apps.farming.models import (AcopioDetalle, ActividadAgricolaItemDetalle,
                                 CierreZafra, CierreZafraDetalle, Zafra)
from apps.inventory.models import Item, ItemMovimiento
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=AcopioDetalle)
def signal_acopio_guardado(sender, instance, created, **kwargs):
    if created:
        item_movimiento = ItemMovimiento()
        item_movimiento.item = instance.acopio.zafra.item
        item_movimiento.deposito = instance.acopio.deposito
        item_movimiento.cantidad = instance.peso
        item_movimiento.costo = 0
        item_movimiento.precio = 0
        item_movimiento.fecha_documento = instance.acopio.fecha
        item_movimiento.secuencia_origen = instance.acopio.pk
        item_movimiento.detalle_secuencia_origen = instance.pk
        item_movimiento.es_vigente = True
        item_movimiento.tipo_movimiento = "AC"
        item_movimiento.save()


@receiver(post_save, sender=ActividadAgricolaItemDetalle)
def signal_actividad_agricola_item_guardado(sender, instance, created, **kwargs):
    if created:
        item_movimiento = ItemMovimiento()
        item_movimiento.item = instance.item
        item_movimiento.deposito = instance.deposito
        item_movimiento.cantidad = instance.cantidad
        item_movimiento.costo = instance.costo
        item_movimiento.precio = 0
        item_movimiento.fecha_documento = instance.actividadAgricola.fechaDocumento
        item_movimiento.secuencia_origen = instance.actividadAgricola.pk
        item_movimiento.detalle_secuencia_origen = instance.pk
        item_movimiento.es_vigente = True
        item_movimiento.tipo_movimiento = "AA"
        item_movimiento.save()


@receiver(post_save, sender=CierreZafra)
def signal_cierre_zafra_save(sender, instance, created, **kwargs):
    if created:
        zafra = Zafra.objects.get(pk=instance.zafra.pk)
        zafra.esta_cerrado = True
        zafra.save()


@receiver(post_save, sender=CierreZafraDetalle)
def signal_cierre_zafra_detalle_guardado(sender, instance, created, **kwargs):
    if created:
        detalle_cierre_zafra = CierreZafraDetalle.objects.filter(
            cierre_zafra=instance.cierre_zafra
        )
        suma_cantidad_acopiada = 0
        suma_costo_total = 0
        costo_unitario = 0
        for x in detalle_cierre_zafra:
            suma_cantidad_acopiada += x.cantidad_acopio_neto
            suma_costo_total += x.costo_total

        if suma_cantidad_acopiada > 0 and suma_costo_total > 0:
            costo_unitario = round(suma_costo_total / suma_cantidad_acopiada)
            item = Item.objects.get(pk=instance.cierre_zafra.zafra.item.pk)
            item.ultimo_costo = costo_unitario
            item.costo = costo_unitario
            item.save()


@receiver(pre_delete, sender=CierreZafra)
def signal_cierre_zafra_borrar(sender, instance, **kwargs):
    zafra = Zafra.objects.get(pk=instance.zafra.pk)
    zafra.esta_cerrado = False
    zafra.save()
