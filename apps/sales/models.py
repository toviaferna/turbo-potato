from django.db import models
from django.utils.html import format_html

from apps.finance.models import Cuenta, Persona
from apps.inventory.models import Deposito, Item


# Create your models here.
class AperturaCaja(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Empleado")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Apertura")
    esta_cerrado = models.BooleanField(verbose_name="Esta Cerrado?",default=False)
    monto_inicio = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Monto Inicial")
    fecha_hora_cierre = models.DateTimeField(auto_now_add=True,null=True, blank=True,verbose_name="Fecha Cierre")

    class Meta:
        verbose_name = "Apertura de caja"
        verbose_name_plural = "Apertura de cajas"

    def __str__(self):
        date_time = self.fecha_hora_registro.strftime("%m/%d/%Y, %H:%M:%S")
        return f"{date_time} Obs: {self.observacion}"

class Arqueo(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Empleado")
    apertura_caja = models.ForeignKey(AperturaCaja, on_delete=models.DO_NOTHING,verbose_name="Apertura Caja")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    monto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Monto Retirado")

class Venta(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cliente")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    apertura_caja = models.ForeignKey(AperturaCaja, on_delete=models.DO_NOTHING,verbose_name="AperturaCaja")
    fecha_documento = models.DateField(verbose_name="Fecha")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    timbrado = models.CharField(max_length=8,verbose_name="Timbrado")
    es_credito = models.BooleanField(verbose_name="Es Crédito?",default=True)
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")

    def get_es_vigente_display(self):
        value = "fa-check" if self.es_vigente else "fa-xmark"
        return format_html(f"<i class='fa-solid {value}'></i>")

    def get_es_credito_display(self):
        value = "fa-check" if self.es_credito else "fa-xmark"
        return format_html(f"<i class='fa-solid {value}'></i>")

    @property
    def total(self):
        return sum(round(x.precio * x.cantidad)  for x in self.ventadetalle_set.all())

    @property
    def imponible5(self):
        return sum(x.imponible5 for x in self.ventadetalle_set.all())

    @property
    def imponible10(self):
        return sum(x.imponible10 for x in self.ventadetalle_set.all())

    @property
    def imponible_exenta(self):
        valor = sum(x.imponible_exenta for x in self.ventadetalle_set.all())
        if valor is None:
            valor = 0
        return valor

    @property
    def iva5(self):
        valor = sum(x.iva5 for x in self.ventadetalle_set.all())
        if valor is None:
            valor = 0
        return valor

    @property
    def iva10(self):
        valor = sum(x.iva10 for x in self.ventadetalle_set.all())
        if valor is None:
            valor = 0
        return valor

    @property
    def total_iva(self):
        return self.iva5+self.iva10

    def __str__(self):
        return self.comprobante+" - "+self.timbrado

class VentaDetalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    costo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo")
    precio = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Precio")
    porcentaje_impuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")
    
    @property
    def subtotal(self):
        return round(self.precio * self.cantidad)
    
    @property
    def subtotal_iva(self):
        if self.porcentaje_impuesto == 5:
            return round((self.costo * self.cantidad) / 21)
        elif self.porcentaje_impuesto == 10:
            return round((self.costo * self.cantidad) / 11)
        else:
            return round((self.costo * self.cantidad) * 0)

    @property
    def imponible5(self):
        if self.porcentaje_impuesto == 5:
            valor = round(self.subtotal)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0
            
    @property
    def imponible10(self):
        if self.porcentaje_impuesto == 10:
            valor = round(self.subtotal)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0
    @property
    def imponible_exenta(self):
        if self.porcentaje_impuesto == 0:
            valor = round(self.subtotal)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0
    @property
    def iva5(self):
        if self.porcentaje_impuesto == 5:
            valor = round(self.subtotal/22)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0
    @property
    def iva10(self):
        if self.porcentaje_impuesto == 10:
            valor = round(self.subtotal/11)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0

class CuotaVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING)
    fecha_vencimiento = models.DateField(verbose_name="Fecha Vencimiento")
    monto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Monto")
    saldo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Saldo",default=0)
    
    class Meta:
        verbose_name = "Cuota de venta"
        verbose_name_plural = "Cuotas de ventas"

class NotaDebitoEmitida(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cliente")
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING,verbose_name="Venta")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    fecha_documento = models.DateField(verbose_name="Fecha Documento")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    timbrado = models.CharField(max_length=8,verbose_name="Timbrado")
    es_credito = models.BooleanField(verbose_name="Es Crédito?",default=False)
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    
    class Meta:
        verbose_name = "Nota de débito emitida"
        verbose_name_plural = "Notas de débito emitidas"
    
    @property
    def total(self):
        return sum(round(x.valor * x.cantidad)  for x in self.notadebitoemitidadetalle_set.all())

class NotaDebitoEmitidaDetalle(models.Model):
    nota_debito_emitida = models.ForeignKey(NotaDebitoEmitida, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    valor = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo/Descuento")
    porcentaje_impuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")

class NotaCreditoEmitida(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cliente")
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING,verbose_name="Venta")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    fecha_documento = models.DateField(verbose_name="Fecha Documento")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    timbrado = models.CharField(max_length=8,verbose_name="Timbrado")
    es_credito = models.BooleanField(verbose_name="Es Crédito?",default=False)
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    
    class Meta:
        verbose_name = "Nota de crédito emitida"
        verbose_name_plural = "Notas de crédito emitidas"

    @property
    def total(self):
        return sum(round(x.valor * x.cantidad)  for x in self.notacreditoemitidadetalle_set.all())

class NotaCreditoEmitidaDetalle(models.Model):
    nota_credito_emitida = models.ForeignKey(NotaCreditoEmitida, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    valor = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo/Descuento")
    es_devolucion = models.BooleanField(verbose_name="Es Devolución?",default=False)
    porcentaje_impuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")
class Cobro(models.Model):
    cobrador = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cobrador",related_name='cobrador')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    apertura_caja = models.ForeignKey(AperturaCaja, on_delete=models.DO_NOTHING,verbose_name="Apertura Caja")
    fecha_documento = models.DateField(verbose_name="Fecha")
    cliente = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cliente",related_name='cliente')
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    monto_a_saldar = models.DecimalField(max_digits=15, decimal_places=0,verbose_name="Monto A Saldar")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")

    def __str__(self):
        return self.comprobante+" - "+self.cliente.razon_social

class CobroDetalle(models.Model):
    cobro = models.ForeignKey(Cobro, on_delete=models.DO_NOTHING)
    cancelacion = models.DecimalField(max_digits=15, decimal_places=0,verbose_name="Cancelacion")
    cuota_venta = models.ForeignKey(CuotaVenta, on_delete=models.DO_NOTHING,verbose_name="Cuota Venta",default= None,null=True)


class CobroMedio(models.Model):
    VALORESENUMTIPMOV = (
        ('CHEQUE DIF', 'CHEQUE DIFERIDO'),
        ('CHEQUE DIA', 'CHEQUE AL DIA'),
        ('EFECTIVO', 'EFECTIVO'),
        ('TRANSFERENCIA', 'TRANSFERENCIA BANCARIA'),
    )
    cobro = models.ForeignKey(Cobro, on_delete=models.DO_NOTHING)
    numero = models.CharField(max_length=15,verbose_name="N°")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    monto = models.DecimalField(max_digits=15, decimal_places=0,verbose_name="Monto")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    medio_cobro = models.CharField(max_length=50,choices=VALORESENUMTIPMOV,verbose_name="Medio Cobro") 
    
    class Meta:
        verbose_name = "Medio de cobro"
        verbose_name_plural = "Medios de cobros"
        
class TransferenciaCuenta(models.Model):
    cuenta_salida = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta Salida",related_name='salida')
    cuenta_entrada = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta Entrada",related_name='entrada')
    apertura_caja = models.ForeignKey(AperturaCaja, on_delete=models.DO_NOTHING,verbose_name="Cuenta Entrada")
    monto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Monto a Transferir")
    fecha = models.DateField(verbose_name="Fecha")
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante", default="" )
    class Meta:
        verbose_name = "Transferencia de cuenta"
        verbose_name_plural = "Transferencias de cuentas"

from .signals import (signal_cobro_anulado, signal_cobro_detalle_save,
                      signal_cobro_pre_guardado,
                      signal_nota_credito_emitida_guardado,
                      signal_pre_guardado_cuota_venta,
                      signal_transferencia_cuenta_pre_guardado,
                      signal_venta_detalle_pre_guardado, signal_venta_guardado,
                      signal_venta_pre_guardado)
