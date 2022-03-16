
from apps.supplies.models import OrdenCompra, PedidoCompra
from core.tables import AccionTable
from django.contrib.humanize.templatetags.humanize import intcomma
import django_tables2 as tables

class PedidoCompraTable(AccionTable):
    class Meta:
        model = PedidoCompra
        fields = ("proveedor","fecha_documento","fecha_vencimiento","es_vigente",)

class OrdenCompraTable(AccionTable):
    
    def render_total(self,value):
        return intcomma(value)
    
    total = tables.Column(verbose_name= 'Total',attrs={
            "td": {"align": "right"},
            "th":{"class":"text-right"},
        } )
    class Meta:
        model = OrdenCompra
        fields = ("proveedor","fecha_documento","total","es_vigente")
        row_attrs = { "registro_es_vigente": lambda record: record.es_vigente }
        order_by = "-fecha_documento"