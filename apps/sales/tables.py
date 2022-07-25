from apps.sales import models
from apps.supplies.models import NotaDebitoRecibida
from core.tables import AccionTable
from core.tables.columns import BooleanColumn, NumericColumn


class AperturaCajaTable(AccionTable):
    monto_inicio = NumericColumn()
    esta_cerrado = BooleanColumn()
    class Meta:
        model = models.AperturaCaja
        fields = ("empleado","fecha_hora_registro","fecha_hora_cierre","monto_inicio","esta_cerrado")

class ArqueoTable(AccionTable):
    monto = NumericColumn(verbose_name= 'Monto')
    class Meta:
        model = models.Arqueo
        fields = ("empleado","apertura_caja","observacion","fecha_hora_registro","monto")

class TransferenciaCuentaTable(AccionTable):
    monto = NumericColumn(verbose_name= 'Monto')
    class Meta:
        model = models.TransferenciaCuenta
        fields = ("fecha","cuenta_salida","cuenta_entrada","monto","es_vigente",)
        row_attrs = {
            "es-vigente": lambda record: record.es_vigente
        }
        order_by = "-fecha"

class VentaTable(AccionTable):
    total = NumericColumn(verbose_name='Total')
    class Meta:
        model = models.Venta
        fields = ("fecha_documento","comprobante","cliente","total","es_vigente",)
        row_attrs = {
            "es-vigente": lambda record: record.es_vigente
        }
        order_by = "-fecha_documento"

class NotaCreditoEmitidaTable(AccionTable):

    total = NumericColumn(verbose_name= 'Total',)
    class Meta:
        model = models.NotaCreditoEmitida
        fields = ("fecha_documento","comprobante","cliente","total","es_vigente",)
        row_attrs = {
            "es-vigente": lambda record: record.es_vigente
        }
        order_by = "-fecha_documento"

class NotaDebitoEmitidaTable(AccionTable):

    total = NumericColumn(verbose_name= 'Total')
    class Meta:
        model = NotaDebitoRecibida
        fields = ("fecha_documento","comprobante","cliente","total","es_vigente",)
        row_attrs = {
            "es-vigente": lambda record: record.es_vigente
        }
        order_by = "-fecha_documento"
