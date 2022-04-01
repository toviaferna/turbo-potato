from django.db.models.signals import post_save,pre_save,pre_delete
from django.dispatch import receiver
from apps.inventory.models import AjusteStockDetalle, Item, ItemMovimiento
from apps.supplies.models import CompraDetalle, NotaCreditoRecibidaDetalle
from apps.farming.models import AcopioDetalle, ActividadAgricolaItemDetalle, CierreZafra, CierreZafraDetalle, Zafra
from apps.sales.models import AperturaCaja, Cobro, CobroDetalle, CuotaVenta, NotaCreditoEmitidaDetalle, TransferenciaCuenta, Venta, VentaDetalle


@receiver(pre_save, sender = CompraDetalle)
def signal_compra_detalle_preguardado(sender, instance, **kwargs):
   pass

@receiver(post_save, sender = CompraDetalle)
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
        item_movimiento.tipo_movimiento = 'CM'
        item_movimiento.save()

        item = Item.objects.get(pk=instance.item.pk)
        item.ultimo_costo = instance.costo
        item.costo = instance.costo
        item.save()

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

@receiver(post_save, sender = AcopioDetalle)
def signalAcopioGuardado(sender, instance, created, **kwargs):
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
        item_movimiento.tipo_movimiento = 'AC'
        item_movimiento.save()

@receiver(post_save, sender = ActividadAgricolaItemDetalle)
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
        item_movimiento.tipo_movimiento = 'AA'
        item_movimiento.save()

@receiver(pre_save, sender = Venta)
def signal_venta_pre_guardado(sender, instance, **kwargs):
    apertura_caja = AperturaCaja.objects.filter(esta_cerrado = False).order_by('-pk')[:1].first()
    timbrado = '12332145'
    instance.apertura_caja = apertura_caja
    instance.timbrado = timbrado

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

@receiver(post_save, sender = NotaCreditoRecibidaDetalle)
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
        item_movimiento.tipo_movimiento = 'DC'
        item_movimiento.save()

@receiver(post_save, sender = NotaCreditoEmitidaDetalle)
def signal_nota_credito_emitida_guardado(sender, instance, created, **kwargs):
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

@receiver(post_save, sender = CierreZafra)
def signal_cierre_zafra_save(sender, instance, created, **kwargs):
    if created:
        zafra = Zafra.objects.get(pk=instance.zafra.pk)
        zafra.esta_cerrado = True
        zafra.save()

@receiver(post_save, sender = CierreZafraDetalle)
def signal_cierre_zafra_detalle_guardado(sender, instance, created, **kwargs):
    if created:
        detalle_cierre_zafra = CierreZafraDetalle.objects.filter(cierre_zafra = instance.cierre_zafra)
        suma_cantidad_acopiada = 0
        suma_costo_total = 0
        costo_unitario = 0
        for x in detalle_cierre_zafra:
            suma_cantidad_acopiada += x.cantidad_acopio_neto
            suma_costo_total += x.costo_total 

        if suma_cantidad_acopiada > 0 and suma_costo_total > 0 :
            costo_unitario = round(suma_costo_total / suma_cantidad_acopiada)
            item = Item.objects.get(pk= instance.cierre_zafra.zafra.item.pk)
            item.ultimo_costo = costo_unitario
            item.costo = costo_unitario
            item.save()

@receiver(pre_delete, sender = CierreZafra)
def signal_cierre_zafra_borrar(sender, instance, **kwargs):
    zafra = Zafra.objects.get(pk=instance.zafra.pk)
    zafra.esta_cerrado = False
    zafra.save()