from apps.supplies.models import PedidoCompra
from apps.supplies.tables import PedidoCompraTable
from core.views import DeleteView, ListView, CreateView, UpdateView
# FINCA
class PedidoCompraListView(ListView):
    model = PedidoCompra
    table_class = PedidoCompraTable
    search_fields = ['proveedor__razon_social',]
    update_url = None #'pedido_compra_update'
    delete_url = None #'pedido_compra_delete'
    create_url = None #'pedido_compra_create'
    page_title = "Pedidos de compras"