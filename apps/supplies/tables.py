
from pyexpat import model
from apps.supplies.models import Compra, CompraDetalle, CuotaCompra, OrdenCompra, PedidoCompra
from core.tables import AccionTable, SingleTable
from core.tables.columns import BooleanColumn, NumberColumn, TotalColumn
from django.contrib.humanize.templatetags.humanize import intcomma
from django.urls.base import reverse
from django.utils.html import format_html

class PedidoCompraTable(AccionTable):
    es_vigente = BooleanColumn()
    class Meta:
        model = PedidoCompra
        fields = ("proveedor","fecha_documento","fecha_vencimiento","es_vigente",)
        row_attrs = { 'es-vigente':lambda record: record.es_vigente }

class OrdenCompraTable(AccionTable):
    es_vigente = BooleanColumn()
    total = NumberColumn(verbose_name="Total")
    class Meta:
        model = OrdenCompra
        fields = ("proveedor","fecha_documento","total","es_vigente")
        row_attrs = { 'es-vigente':lambda record: record.es_vigente }
        order_by = "-fecha_documento"

class CompraTable(AccionTable):
    es_credito = BooleanColumn()
    es_vigente = BooleanColumn()
    total = NumberColumn(verbose_name="Total")
    
    def render_comprobante(self, value, record):
            if record.es_vigente:
                return format_html('<a href="{}">{}</a>',reverse('compra_detail',kwargs={'pk': record.pk}),value)
            else:
                return value
    class Meta:
        model = Compra
        fields = ("fecha_documento","comprobante","proveedor","es_credito","total","es_vigente",)
        row_attrs = { 'es-vigente':lambda record: record.es_vigente }
        order_by = "-fecha_documento"
    
class CompraDetalleTable(SingleTable):
    subtotal = TotalColumn(verbose_name="Subtotal")
    subtotal_iva = TotalColumn(verbose_name="Subtotal IVA")

    class Meta:
        model = CompraDetalle
        orderable = False
        fields = ("item__pk","cantidad","item__descripcion","costo","porcentaje_impuesto", "subtotal","subtotal_iva")
        attrs = {
            "class":"table table-sm table-striped"
        }
class CuotaCompraTable(SingleTable):
    monto = TotalColumn()
    class Meta:
        model = CuotaCompra
        fields = ("fecha_vencimiento", "monto")
        attrs = {
            "class":"table table-sm table-striped "
        }
