from django.urls.base import reverse
from django.utils.html import format_html

from apps.supplies import models
from core.tables import AccionTable, DetailTable
from core.tables.columns import BooleanColumn, NumericColumn


class PedidoCompraTable(AccionTable):
    es_vigente = BooleanColumn()
    #id = tables.Column(verbose_name='ID', accessor=Accessor('pk'))

    def render_proveedor(self, value, record):
        return format_html(
            '<a href="{}">{}</a>',
            reverse("pedido_compra_detail", kwargs={"pk": record.pk}),
            value,
        )
    class Meta:
        model = models.PedidoCompra
        fields = (
            "pk",
            "proveedor",
            "fecha_documento",
            "fecha_vencimiento",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"

class OrdenCompraTable(AccionTable):
    es_vigente = BooleanColumn()
    total = NumericColumn(verbose_name="Total")
    def render_proveedor(self, value, record):
        return format_html(
            '<a href="{}">{}</a>',
            reverse("orden_compra_detail", kwargs={"pk": record.pk}),
            value,
        )

    class Meta:
        model = models.OrdenCompra
        fields = ("pk","proveedor", "fecha_documento", "total", "es_vigente")
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"

class CompraTable(AccionTable):
    es_credito = BooleanColumn()
    es_vigente = BooleanColumn()
    total = NumericColumn(verbose_name="Total")

    def render_comprobante(self, value, record):
        if record.es_vigente:
            return format_html(
                '<a href="{}">{}</a>',
                reverse("compra_detail", kwargs={"pk": record.pk}),
                value,
            )
        else:
            return value

    class Meta:
        model = models.Compra
        fields = (
            "fecha_documento",
            "comprobante",
            "proveedor",
            "es_credito",
            "total",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"


class CompraDetalleTable(DetailTable):
    cantidad = NumericColumn()
    costo = NumericColumn()
    subtotal = NumericColumn(verbose_name="Subtotal")
    subtotal_iva = NumericColumn(verbose_name="Subtotal IVA")
    porcentaje_impuesto = NumericColumn()

    class Meta:
        model = models.CompraDetalle
        fields = (
            "item__pk",
            "cantidad",
            "item__descripcion",
            "costo",
            "porcentaje_impuesto",
            "subtotal",
            "subtotal_iva",
        )


class CuotaCompraTable(DetailTable):
    monto = NumericColumn()

    class Meta:
        model = models.CuotaCompra
        fields = ("fecha_vencimiento", "monto")


class NotaDebitoRecibidaTable(AccionTable):
    total = NumericColumn()
    es_vigente = BooleanColumn()

    class Meta:
        model = models.NotaDebitoRecibida
        fields = (
            "fecha_documento",
            "comprobante",
            "proveedor",
            "total",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"


class NotaCreditoRecibidaTable(AccionTable):
    total = NumericColumn()
    es_vigente = BooleanColumn()

    class Meta:
        model = models.NotaCreditoRecibida
        fields = (
            "fecha_documento",
            "comprobante",
            "proveedor",
            "total",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"


class LibroCompraTable(DetailTable):
    iva5 = NumericColumn()
    iva10 = NumericColumn()
    imponible_exenta = NumericColumn()
    imponible5 = NumericColumn()
    imponible10 = NumericColumn()
    total = NumericColumn()

    class Meta:
        model = models.Compra
        fields = (
            "fecha_documento",
            "es_credito",
            "comprobante",
            "proveedor",
            "iva5",
            "iva10",
            "imponible_exenta",
            "imponible5",
            "imponible10",
            "total",
        )

class PedidoCompraDetalleTable(DetailTable):
    cantidad = NumericColumn()

    class Meta:
        model = models.PedidoCompraDetalle
        fields = (
            "item__pk",
            "item__descripcion",
            "cantidad",
        )

class OrdenCompraDetalleTable(DetailTable):
    cantidad = NumericColumn()
    precio = NumericColumn()
    descuento = NumericColumn()
    subtotal = NumericColumn()

    class Meta:
        model = models.OrdenCompraDetalle
        fields = (
            "item__pk",
            "item__descripcion",
            "cantidad",
            "precio",
            "descuento",
            "subtotal"
        )