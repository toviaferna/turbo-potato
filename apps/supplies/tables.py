
from apps.supplies.models import PedidoCompra
from core.tables import AccionTable

class PedidoCompraTable(AccionTable):
    class Meta:
        model = PedidoCompra
        fields = ("proveedor","fecha_documento","fecha_vencimiento","es_vigente",)