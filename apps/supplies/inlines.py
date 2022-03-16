from extra_views import InlineFormSetFactory
from apps.supplies.forms import OrdenCompraDetalleForm, PedidoCompraDetalleForm
from apps.supplies.models import OrdenCompraDetalle, PedidoCompraDetalle

class PedidoCompraDetalleInline(InlineFormSetFactory):
    model = PedidoCompraDetalle
    form_class = PedidoCompraDetalleForm
    factory_kwargs = { 'extra':1, }
    fields =  ['item','cantidad']

class OrdenCompraDetalleInline(InlineFormSetFactory):
    model = OrdenCompraDetalle
    form_class = OrdenCompraDetalleForm
    factory_kwargs = { 'extra':1, }
    fields = ['item', 'cantidad','precio','descuento']