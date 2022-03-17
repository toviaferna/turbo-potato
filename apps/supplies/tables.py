
from apps.supplies.models import OrdenCompra, PedidoCompra
from core.tables import AccionTable, columns
from core.tables.columns import BooleanColumn, NumberColumn
from django.contrib.humanize.templatetags.humanize import intcomma
import django_tables2 as tables

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