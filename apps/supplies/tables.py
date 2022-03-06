
from apps.supplies.models import PedidoCompra
from core.tables import EditableTable

class PedidoCompraTable(EditableTable):
    class Meta:
        model = PedidoCompra
        fields = ("proveedor","fecha_documento","fecha_vencimiento","es_vigente",)