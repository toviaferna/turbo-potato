from django.urls.base import reverse
from django.utils.html import format_html

from apps.finance.models import Persona
from apps.sales import models
from apps.supplies.models import NotaDebitoRecibida
from core.tables import AccionTable, DetailTable
from core.tables.columns import (BooleanColumn, NumericColumn,
                                 TotalNumericColumn)


class AperturaCajaTable(AccionTable):
    monto_inicio = NumericColumn()
    esta_cerrado = BooleanColumn()

    class Meta:
        model = models.AperturaCaja
        fields = (
            "empleado",
            "fecha_hora_registro",
            "fecha_hora_cierre",
            "monto_inicio",
            "esta_cerrado",
        )


class ArqueoTable(AccionTable):
    monto = NumericColumn(verbose_name="Monto")

    class Meta:
        model = models.Arqueo
        fields = (
            "empleado",
            "apertura_caja",
            "observacion",
            "fecha_hora_registro",
            "monto",
        )


class TransferenciaCuentaTable(AccionTable):
    monto = NumericColumn(verbose_name="Monto")

    class Meta:
        model = models.TransferenciaCuenta
        fields = (
            "fecha",
            "cuenta_salida",
            "cuenta_entrada",
            "monto",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha"


class VentaTable(AccionTable):
    total = NumericColumn(verbose_name="Total")
    es_vigente = BooleanColumn()
    
    def render_comprobante(self, value, record):
        return format_html(
            '<a href="{}">{}</a>',
            reverse("venta_detail", kwargs={"pk": record.pk}),
            value,
        )

    class Meta:
        model = models.Venta
        fields = (
            "fecha_documento",
            "comprobante",
            "cliente",
            "total",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"

class VentaDetalleTable(DetailTable):
    cantidad = NumericColumn()
    precio = NumericColumn()
    subtotal = NumericColumn(verbose_name="Subtotal")
    subtotal_iva = NumericColumn(verbose_name="Subtotal IVA")
    porcentaje_impuesto = NumericColumn()

    class Meta:
        model = models.VentaDetalle
        fields = (
            "item__pk",
            "cantidad",
            "item__descripcion",
            "precio",
            "porcentaje_impuesto",
            "subtotal",
            "subtotal_iva",
        )

class NotaCreditoDetalleTable(DetailTable):
    cantidad = NumericColumn()
    valor = NumericColumn()
    subtotal = NumericColumn(verbose_name="Subtotal")

    class Meta:
        model = models.NotaCreditoEmitidaDetalle
        fields = (
            "item__pk",
            "cantidad",
            "item__descripcion",
            "valor",
            "subtotal",
        )


class CuotaVentaTable(DetailTable):
    monto = NumericColumn()

    class Meta:
        model = models.CuotaVenta
        fields = ("fecha_vencimiento", "monto")
        
class NotaCreditoEmitidaTable(AccionTable):

    def render_comprobante(self, value, record):
        return format_html(
            '<a href="{}">{}</a>',
            reverse("nota_credito_emitida_detail", kwargs={"pk": record.pk}),
            value,
        )

    total = NumericColumn(
        verbose_name="Total",
    )
    es_vigente = BooleanColumn()
    class Meta:
        model = models.NotaCreditoEmitida
        fields = (
            "fecha_documento",
            "comprobante",
            "cliente",
            "total",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"


class NotaDebitoEmitidaTable(AccionTable):

    total = NumericColumn(verbose_name="Total")
    es_vigente = BooleanColumn()
    class Meta:
        model = NotaDebitoRecibida
        fields = (
            "fecha_documento",
            "comprobante",
            "cliente",
            "total",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"


class CobroTable(AccionTable):
    es_vigente = BooleanColumn()
    monto_a_saldar = NumericColumn(
        verbose_name="Total",
    )

    class Meta:
        model = models.Cobro
        fields = (
            "fecha_documento",
            "comprobante",
            "cuenta",
            "cliente",
            "cobrador",
            "monto_a_saldar",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"


class CobroPersonaSelectionTable(AccionTable):
    class Meta:
        model = Persona
        fields = (
            "razon_social",
            "documento",
        )


class LibroVentaTable(DetailTable):

    iva5 = NumericColumn(
        verbose_name="Iva 5",
    )
    iva10 = NumericColumn(
        verbose_name="Iva 10",
    )
    imponible_exenta = NumericColumn(
        verbose_name="Imp. Exenta",
    )
    imponible5 = NumericColumn(
        verbose_name="Imp. 5",
    )
    imponible10 = NumericColumn(
        verbose_name="Imp. 10",
    )
    total = NumericColumn(
        verbose_name="Imp. Total",
    )

    class Meta:
        model = models.Venta
        fields = (
            "fecha_documento",
            "es_credito",
            "comprobante",
            "cliente",
            "iva5",
            "iva10",
            "imponible_exenta",
            "imponible5",
            "imponible10",
            "total",
        )

class EstablecimientoTable(AccionTable):
    class Meta:
        model = models.Establecimiento
        fields = ("id", "descripcion")

class TipoDocumentoTable(AccionTable):
    class Meta:
        model = models.TipoDocumento
        fields = ("id", "descripcion")

class PuntoExpedicionTable(AccionTable):
    class Meta:
        model = models.PuntoExpedicion
        fields = ("id", "establecimiento", "descripcion")

class TimbradoTable(AccionTable):
    class Meta:
        model = models.Timbrado
        fields = ("id", "numero","tipo_documento", "punto_expedicion", "inicio_vigencia", "fin_vigencia","es_vigente")