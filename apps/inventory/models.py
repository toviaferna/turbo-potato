from django.db import models

from apps.finance.models import Persona, TipoImpuesto


class Marca(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class Categoria(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class Deposito(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    es_planta_acopiadora = models.BooleanField(verbose_name="Es Planta Acopiadora?",default=False)
    def __str__(self):
        return self.descripcion

class TipoItem(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    
    class Meta:
        verbose_name = "Tipo de item"
        verbose_name_plural = "Tipos de items"

    def __str__(self):
        return self.descripcion

class Item(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo",default=0)
    ultimo_costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ult. Costo",default=0)
    es_activo = models.BooleanField(verbose_name="Activo?")
    codigo_barra = models.CharField(max_length=20, verbose_name="Cód Barra")
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING, verbose_name="Marca")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, verbose_name="Categoria")
    tipo_item = models.ForeignKey(TipoItem, on_delete=models.DO_NOTHING, verbose_name="Tipo Item")
    tipo_impuesto = models.ForeignKey(TipoImpuesto, on_delete=models.DO_NOTHING, verbose_name="Tipo Imp.")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion


class ItemMovimiento(models.Model):
    VALORESENUMTIPMOV = (
        ('CM', 'COMPRAS'),
        ('VT', 'VENTAS'),
        ('A+', 'AJUSTES STOCK +'),
        ('A-', 'AJUSTES STOCK -'),
        ('AC', 'ACOPIOS'),
        ('AA', 'ACTIVIDADES AGRICOLAS'),
        ('DC', 'DEVOLUCIONES DE COMPRAS'),
        ('DV', 'DEVOLUCIONES DE VENTAS'),
    )
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    costo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo")
    precio = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Precio")
    fecha_documento = models.DateField(verbose_name="Fecha Documento")
    secuencia_origen = models.IntegerField()
    detalle_secuencia_origen = models.IntegerField()
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True) 
    tipo_movimiento = models.CharField(max_length=50,choices=VALORESENUMTIPMOV,verbose_name="Tipo Mov.") 


class AjusteStock(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Empleado")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito")
    fecha_documento = models.DateField(verbose_name="Fecha")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    comprobante = models.CharField(max_length=15,verbose_name="Comprobante")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")

class AjusteStockDetalle(models.Model):
    ajuste_stock = models.ForeignKey(AjusteStock, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")

from .signals import signal_ajuste_stock_guardado
