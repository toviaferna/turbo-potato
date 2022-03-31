from django.db import models

from apps.finance.models import Cuenta, Persona
from apps.inventory.models import Deposito, Item

# Create your models here.
class AperturaCaja(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Empleado")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    fechaHoraRegistro = models.DateTimeField(auto_now_add=True,verbose_name="Fec Hr Apertura")
    estaCerrado = models.BooleanField(verbose_name="Esta Cerrado?",default=False)
    montoInicio = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Monto Apertura")
    fechaHoraCierre = models.DateTimeField(auto_now_add=True,null=True, blank=True,verbose_name="Fec Hr Cierre")
    def __str__(self):
        date_time = self.fechaHoraRegistro.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time+" Obs: "+self.observacion

class Arqueo(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Empleado")
    aperturaCaja = models.ForeignKey(AperturaCaja, on_delete=models.DO_NOTHING,verbose_name="Apertura Caja")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    fechaHoraRegistro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    monto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Monto Retirado")

class Venta(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cliente")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    aperturaCaja = models.ForeignKey(AperturaCaja, on_delete=models.DO_NOTHING,verbose_name="AperturaCaja")
    fechaDocumento = models.DateField(verbose_name="Fecha")
    fechaHoraRegistro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    timbrado = models.CharField(max_length=8,verbose_name="Timbrado")
    esCredito = models.BooleanField(verbose_name="Es Crédito?",default=True)
    esVigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
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
    def imponibleExenta(self):
        valor = sum(x.imponibleExenta for x in self.ventadetalle_set.all())
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
    def totalIva(self):
        return self.iva5+self.iva10

    def __str__(self):
        return self.comprobante+" - "+self.timbrado

class VentaDetalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    costo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo")
    precio = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Precio")
    porcentajeImpuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")
    @property
    def subtotal(self):
        return round(self.precio * self.cantidad)
    @property
    def imponible5(self):
        if self.porcentajeImpuesto == 5:
            valor = round(self.subtotal)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0
    @property
    def imponible10(self):
        if self.porcentajeImpuesto == 10:
            valor = round(self.subtotal)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0
    @property
    def imponibleExenta(self):
        if self.porcentajeImpuesto == 0:
            valor = round(self.subtotal)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0
    @property
    def iva5(self):
        if self.porcentajeImpuesto == 5:
            valor = round(self.subtotal/22)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0
    @property
    def iva10(self):
        if self.porcentajeImpuesto == 10:
            valor = round(self.subtotal/11)
            if valor is None:
                valor = 0
            return valor
        else:
            return 0

class CuotaVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING)
    fechaVencimiento = models.DateField(verbose_name="Fecha Vencimiento")
    monto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Monto")
    saldo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Saldo",default=0)

class NotaDebitoEmitida(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cliente")
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING,verbose_name="Venta")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    fechaDocumento = models.DateField(verbose_name="Fecha Documento")
    fechaHoraRegistro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    timbrado = models.CharField(max_length=8,verbose_name="Timbrado")
    esCredito = models.BooleanField(verbose_name="Es Crédito?",default=False)
    esVigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    @property
    def total(self):
        return sum(round(x.valor * x.cantidad)  for x in self.notadebitoemitidadetalle_set.all())

class NotaDebitoEmitidaDetalle(models.Model):
    notaDebitoEmitida = models.ForeignKey(NotaDebitoEmitida, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    valor = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo/Descuento")
    porcentajeImpuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")

class NotaCreditoEmitida(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cliente")
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING,verbose_name="Venta")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    fechaDocumento = models.DateField(verbose_name="Fecha Documento")
    fechaHoraRegistro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    timbrado = models.CharField(max_length=8,verbose_name="Timbrado")
    esCredito = models.BooleanField(verbose_name="Es Crédito?",default=False)
    esVigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    @property
    def total(self):
        return sum(round(x.valor * x.cantidad)  for x in self.notacreditoemitidadetalle_set.all())

class NotaCreditoEmitidaDetalle(models.Model):
    notaCreditoEmitida = models.ForeignKey(NotaCreditoEmitida, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    valor = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo/Descuento")
    esDevolucion = models.BooleanField(verbose_name="Es Devolución?",default=False)
    porcentajeImpuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")
class Cobro(models.Model):
    cobrador = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cobrador",related_name='cobrador')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta")
    aperturaCaja = models.ForeignKey(AperturaCaja, on_delete=models.DO_NOTHING,verbose_name="Apertura Caja")
    fechaDocumento = models.DateField(verbose_name="Fecha")
    cliente = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Cliente",related_name='cliente')
    fechaHoraRegistro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    esVigente = models.BooleanField(verbose_name="Vigente?",default=True)
    montoASaldar = models.DecimalField(max_digits=15, decimal_places=0,verbose_name="Monto A Saldar")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
class CobroDetalle(models.Model):
    cobro = models.ForeignKey(Cobro, on_delete=models.DO_NOTHING)
    cancelacion = models.DecimalField(max_digits=15, decimal_places=0,verbose_name="Cancelacion")
    cuotaVenta = models.ForeignKey(CuotaVenta, on_delete=models.DO_NOTHING,verbose_name="Cuota Venta",default= None,null=True)


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
    medioCobro = models.CharField(max_length=50,choices=VALORESENUMTIPMOV,verbose_name="Medio Cobro") 

class TransferenciaCuenta(models.Model):
    cuentaSalida = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta Salida",related_name='salida')
    cuentaEntrada = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING,verbose_name="Cuenta Entrada",related_name='entrada')
    aperturaCaja = models.ForeignKey(AperturaCaja, on_delete=models.DO_NOTHING,verbose_name="Cuenta Entrada")
    monto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Monto a Transferir")
    fecha = models.DateField(verbose_name="Fecha")
    esVigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante", default="" )




