from extra_views import InlineFormSetFactory
from apps.supplies.forms import CompraDetalleForm, CuotaCompraForm, NotaDebitoRecibidaDetalleForm, OrdenCompraDetalleForm, PedidoCompraDetalleForm
from apps.supplies.models import CompraDetalle, CuotaCompra, NotaDebitoRecibidaDetalle, OrdenCompraDetalle, PedidoCompraDetalle
from core.widgets import ItemCustomSelect
from django.forms import widgets

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

class CompraDetalleInline(InlineFormSetFactory):
    model = CompraDetalle
    form_class = CompraDetalleForm
    factory_kwargs = {
        'extra':1 ,
        'widgets':{
            'item':ItemCustomSelect(
                attrs={
                    'wrapper_class':'col-sm-4',
                    'data-item-select':True,

                }
            ),
            'cantidad':widgets.NumberInput(
                attrs={
                    'wrapper_class':'col-sm-1',
                    'class':'text-right',
                }
            ),
            'costo':widgets.NumberInput(
                attrs={
                    'class':'text-right item-costo',
                }
            ),
            'porcentaje_impuesto':widgets.NumberInput(
                attrs={
                    'class':'text-right item-porcentaje-impuesto',
                }
            ),
        }
    }
    fields = ['item', 'cantidad','costo','porcentaje_impuesto',]

class CuotaCompraInline(InlineFormSetFactory):
    model = CuotaCompra
    form_class =CuotaCompraForm
    factory_kwargs = {'extra':1 }
    fields = ['fecha_vencimiento','monto']

class NotaDebitoRecibidaDetalleInline(InlineFormSetFactory):
    model = NotaDebitoRecibidaDetalle
    form_class = NotaDebitoRecibidaDetalleForm
    factory_kwargs = {
        'extra':1,
        'widgets':{
            'item':ItemCustomSelect(
                attrs={
                    'wrapper_class':'col-sm-3',
                    'data-item-select':True,
                }
            ),
            'porcentaje_impuesto':widgets.NumberInput(
                attrs={
                    'class':'text-right item-porcentaje-impuesto',
                }
            ),
            'valor':widgets.NumberInput(
                attrs={
                    'class':'text-right item-costo',
                }
            ),
            'cantidad':widgets.NumberInput(
                attrs={
                    'wrapper_class':'col-sm-1',
                }
            ),
        }
    }
    fields = ['item', 'cantidad','valor','porcentaje_impuesto',]