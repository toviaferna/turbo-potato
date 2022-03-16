from apps.supplies.forms import OrdenCompraForm, PedidoCompraForm
from apps.supplies.models import OrdenCompra, PedidoCompra
from apps.supplies.tables import OrdenCompraTable, PedidoCompraTable
from core.views import AnnulledView, CreateView, ListView, UpdateView
from apps.supplies.inlines import OrdenCompraDetalleInline, PedidoCompraDetalleInline

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

class OrdenCompraListView(ListView):
    model = OrdenCompra
    table_class = OrdenCompraTable
    search_fields = ['proveedor__razon_social',]
    update_url = None
    delete_url = 'orden_compra_delete'
    create_url = "orden_compra_create"
    page_title = "Pedidos de compras"

class OrdenCompraCreateView(CreateView):
    model = OrdenCompra
    form_class = OrdenCompraForm
    inlines = [OrdenCompraDetalleInline]
    page_title = "Agregar orden de compra"
    list_url = "orden_compra_list"

class OrdenCompraAnnulledView(AnnulledView):
    model = OrdenCompra
    page_title = "Anular orden de compra"
    list_url = "orden_compra_list"

