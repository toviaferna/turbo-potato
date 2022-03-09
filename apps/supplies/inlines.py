from extra_views import InlineFormSetFactory
from apps.supplies.forms import PedidoCompraDetalleForm
from django.forms import widgets
from apps.supplies.models import PedidoCompraDetalle

class PedidoCompraDetalleInline(InlineFormSetFactory):
    model = PedidoCompraDetalle
    form_class = PedidoCompraDetalleForm
    factory_kwargs = {
        'extra':1,
        'widgets':{
            'item':widgets.Select(
                attrs={
                    'wrapper_class':'col-sm-10',
                }
            ),
            'cantidad':widgets.NumberInput(
                attrs={
                    'wrapper_class':'col-sm-2',
                    'class':'text-right',
                }
            ),
        }
    }
    fields =  ['item','cantidad']