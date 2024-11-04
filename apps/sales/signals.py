from django.conf import settings
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from apps.inventory.models import ItemMovimiento
from apps.sales.models import (AperturaCaja, Cobro, CobroDetalle, CuotaVenta,
                               NotaCreditoEmitida, NotaCreditoEmitidaDetalle,
                               NotaDebitoEmitida, Timbrado,
                               TransferenciaCuenta, Venta, VentaDetalle)


@receiver(pre_save, sender = Venta)
def signal_venta_pre_guardado(sender, instance, **kwargs):
    apertura_caja = AperturaCaja.objects.filter(esta_cerrado = False).order_by('-pk')[:1].first()
    instance.apertura_caja = apertura_caja
    instance.timbrado = Timbrado.objects.filter(es_vigente = True, tipo_documento=1).first().numero

@receiver(pre_save, sender = NotaCreditoEmitida)
def signal_nota_credito_emitida_pre_guardado(sender, instance, **kwargs):
    instance.timbrado = Timbrado.objects.filter(es_vigente = True, tipo_documento=2).first().numero

@receiver(pre_save, sender = NotaDebitoEmitida)
def signal_nota_debito_emitida_pre_guardado(sender, instance, **kwargs):
    instance.timbrado = Timbrado.objects.filter(es_vigente = True, tipo_documento=3).first().numero

@receiver(pre_save, sender = TransferenciaCuenta)
def signal_transferencia_cuenta_pre_guardado(sender, instance, **kwargs):
    apertura_caja = AperturaCaja.objects.filter(esta_cerrado = False).order_by('-pk')[:1].first()
    instance.aperturaCaja = apertura_caja

@receiver(pre_save, sender = VentaDetalle)
def signal_venta_detalle_pre_guardado(sender, instance, **kwargs):
   instance.costo = instance.item.costo

@receiver(post_save, sender = VentaDetalle)
def signal_venta_guardado(sender, instance, created, **kwargs):
    if created:
        item_movimiento = ItemMovimiento()
        item_movimiento.item = instance.item
        item_movimiento.deposito = instance.venta.deposito
        item_movimiento.cantidad = instance.cantidad
        item_movimiento.costo = instance.costo
        item_movimiento.precio = instance.precio
        item_movimiento.fecha_documento = instance.venta.fecha_documento
        item_movimiento.secuencia_origen = instance.venta.pk
        item_movimiento.detalle_secuencia_origen = instance.pk
        item_movimiento.es_vigente = True
        item_movimiento.tipo_movimiento = 'VT'
        item_movimiento.save()

@receiver(post_save, sender = NotaCreditoEmitidaDetalle)
def signal_nota_credito_emitida_detalle_guardado(sender, instance, created, **kwargs):
    if created:
        item_movimiento = ItemMovimiento()
        item_movimiento.item = instance.item
        item_movimiento.deposito = instance.nota_credito_emitida.deposito
        item_movimiento.cantidad = instance.cantidad
        item_movimiento.costo = instance.item.costo
        item_movimiento.precio = instance.valor
        item_movimiento.fecha_documento = instance.nota_credito_emitida.fecha_documento
        item_movimiento.secuencia_origen = instance.nota_credito_emitida.pk
        item_movimiento.detalle_secuencia_origen = instance.pk
        item_movimiento.es_vigente = True
        item_movimiento.tipo_movimiento = 'DV'
        item_movimiento.save()

@receiver(pre_save, sender = Cobro)
def signal_cobro_pre_guardado(sender, instance, **kwargs):
    apertura_caja = AperturaCaja.objects.filter(esta_cerrado = False).order_by('-pk')[:1].first()
    instance.apertura_caja = apertura_caja

@receiver(pre_save, sender = CuotaVenta)
def signal_pre_guardado_cuota_venta(sender, instance, **kwargs):
    if instance.pk is None:
        instance.saldo =  instance.monto

@receiver(post_save, sender = CobroDetalle)
def signal_cobro_detalle_save(sender, instance, created, **kwargs):
    if created:
        cuota = CuotaVenta.objects.get(pk=instance.cuota_venta.pk)
        cuota.saldo = cuota.saldo - instance.cancelacion
        cuota.save()

@receiver(post_save, sender = Cobro)
def signal_cobro_anulado(sender, instance, created, **kwargs):
    print("entra en la señal")
    if created == False:
        cobro_detalle = CobroDetalle.objects.filter(cobro__pk = instance.pk)
        for f in cobro_detalle:
            cuota_venta = CuotaVenta.objects.get(pk = f.cuota_venta.pk)
            cuota_venta.saldo =  cuota_venta.saldo + f.cancelacion  
            cuota_venta.save()
    else: 
         print("entra en la señal create true")
