from apps.finance.models import Cuenta, Persona
from apps.inventory.models import Deposito, Item
from django.db import models
from django.utils.html import format_html

# Create your models here.
class PedidoCompra(models.Model):
    proveedor = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Proveedor")
    fecha_documento = models.DateField(verbose_name="Fecha Documento")
    fecha_vencimiento = models.DateField(verbose_name="Fecha Vencimiento")
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    class Meta:
        verbose_name = "Pedido de compra"
        verbose_name_plural = "Pedidos de compras"

    def __str__(self):
        return self.proveedor.razon_social+" - "+"" if not self.observacion else self.observacion

    @property
    def total(self):
        return sum(round(x.cantidad)  for x in self.pedidocompradetalle_set.all())

class PedidoCompraDetalle(models.Model):
    pedido_compra = models.ForeignKey(PedidoCompra, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")

class OrdenCompra(models.Model):
    pedido_compra = models.ForeignKey(PedidoCompra, on_delete=models.DO_NOTHING,verbose_name="Pedido Compra")
    proveedor = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Proveedor")
    fecha_documento = models.DateField(verbose_name="Fecha Documento")
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    
    class Meta:
        verbose_name = "Orden de compra"
        verbose_name_plural = "Ordenes de compras"
    
    @property
    def total(self):
        return sum(round(x.precio*x.cantidad)  for x in self.ordencompradetalle_set.all())

class OrdenCompraDetalle(models.Model):
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    precio = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Precio")
    descuento = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Descuento")

class Compra(models.Model):
    proveedor = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Proveedor")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    fecha_documento = models.DateField(verbose_name="Fecha Documento")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    timbrado = models.CharField(max_length=8,verbose_name="Timbrado")
    es_credito = models.BooleanField(verbose_name="Es Crédito?",default=True)
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    
    def get_es_vigente_display(self):
        value =  'fa-check' if self.es_vigente else 'fa-xmark'
        return format_html(f"<i class='fa-solid {value}'></i>")
    
    def get_es_credito_display(self):
        value =  'fa-check' if self.es_credito else 'fa-xmark'
        return format_html(f"<i class='fa-solid {value}'></i>")

    @property
    def total(self):
        return sum(round(x.costo * x.cantidad)  for x in self.compradetalle_set.all())
    
    def __str__(self):
        return self.comprobante+" - "+self.timbrado+" - "+self.proveedor.razon_social
    
    @property
    def imponible5(self):
        return sum(x.imponible5 for x in self.compradetalle_set.all())
    
    @property
    def imponible10(self):
        return sum(x.imponible10 for x in self.compradetalle_set.all())
    
    @property
    def imponible_exenta(self):
        valor = sum(x.imponible_exenta for x in self.compradetalle_set.all())
        if valor is None:
            valor = 0
        return valor
    
    @property
    def iva5(self):
        valor = sum(x.iva5 for x in self.compradetalle_set.all())
        if valor is None:
            valor = 0
        return valor
    
    @property
    def iva10(self):
        valor = sum(x.iva10 for x in self.compradetalle_set.all())
        if valor is None:
            valor = 0
        return valor
    
    @property
    def total_iva(self):
        return self.iva5+self.iva10

class CompraDetalle(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    costo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo")
    porcentaje_impuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")
    
    @property
    def subtotal(self):
        return round(self.costo * self.cantidad)
    
    @property
    def subtotal_iva(self):
        if self.porcentaje_impuesto == 5:
            return round((self.costo * self.cantidad)/21)
        elif self.porcentaje_impuesto == 10:
            return round((self.costo * self.cantidad)/11)
        else:
            return round((self.costo * self.cantidad)*0)
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

class CuotaCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.DO_NOTHING)
    fecha_vencimiento = models.DateField(verbose_name="Fecha Vencimiento")
    monto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Monto")
    saldo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Saldo",default=0)
    class Meta:
        verbose_name = "Cuota de compra"
        verbose_name_plural = "Cuotas de compras"

class NotaCreditoRecibida(models.Model):
    proveedor = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Proveedor")
    compra = models.ForeignKey(Compra, on_delete=models.DO_NOTHING,verbose_name="Compra")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    fecha_documento = models.DateField(verbose_name="Fecha")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    timbrado = models.CharField(max_length=8,verbose_name="Timbrado")
    es_credito = models.BooleanField(verbose_name="Es Crédito?",default=False)
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    
    class Meta:
        verbose_name = "Nota de crédito recibida"
        verbose_name_plural = "Notas de crédito recibidas"
    
    @property
    def total(self):
        return sum(round(x.valor * x.cantidad)  for x in self.notacreditorecibidadetalle_set.all())

class NotaCreditoRecibidaDetalle(models.Model):
    nota_credito_recibida = models.ForeignKey(NotaCreditoRecibida, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    valor = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo/Descuento")
    es_devolucion = models.BooleanField(verbose_name="Es Devolución?",default=False)
    porcentaje_impuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")

class NotaDebitoRecibida(models.Model):
    proveedor = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Proveedor")
    compra = models.ForeignKey(Compra, on_delete=models.DO_NOTHING,verbose_name="Compra")
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
        verbose_name = "Nota de débito recibida"
        verbose_name_plural = "Notas de débito recibidas"
    
    def __str__(self):
        return self.comprobante+" - "+self.timbrado+" - "+self.proveedor.razon_social
    
    @property
    def total(self):
        return sum(round(x.valor * x.cantidad)  for x in self.notadebitorecibidadetalle_set.all())

class NotaDebitoRecibidaDetalle(models.Model):
    nota_debito_recibida = models.ForeignKey(NotaDebitoRecibida, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    valor = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Precio/Aumento")
    porcentaje_impuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")


from .signals import (signal_compra_guardado,
                      signal_nota_credito_recibida_guardado)
