from apps.supplies.forms import PedidoCompraForm
from apps.supplies.models import PedidoCompra
from apps.supplies.tables import PedidoCompraTable
from core.views import CreateView, ListView, UpdateView
from apps.supplies.inlines import PedidoCompraDetalleInline

class PedidoCompraListView(ListView):
    model = PedidoCompra
    table_class = PedidoCompraTable
    search_fields = ['proveedor__razon_social',]
    update_url = 'pedido_compra_update'
    delete_url = None
    create_url = "pedido_compra_create"
    page_title = "Pedidos de compras"

class PedidoCompraCreateView(CreateView):
    model = PedidoCompra
    form_class = PedidoCompraForm
    inlines = [PedidoCompraDetalleInline]
    page_title = "Agregar pedidos de compras"
    list_url = "pedido_compra_list"

class PedidoCompraUpdateView(UpdateView):
    model = PedidoCompra
    form_class = PedidoCompraForm
    inlines = [PedidoCompraDetalleInline]
    page_title = "Agregar pedidos de compras"
    list_url = "pedido_compra_list"

