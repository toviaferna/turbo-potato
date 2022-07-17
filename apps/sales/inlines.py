from apps.sales import forms, models
from core.widgets import ItemCustomSelect
from django.forms import widgets
from extra_views import InlineFormSetFactory


class CuotaVentaInline(InlineFormSetFactory):
    model = models.CuotaVenta
    form_class = forms.CuotaVentaForm
    factory_kwargs = {'extra':1 }
    fields = ['fecha_vencimiento','monto']

class VentaDetalleInline(InlineFormSetFactory):
    model = models.VentaDetalle
    form_class = forms.VentaDetalleForm
    factory_kwargs = {
        'extra':1,
        'widgets':{
            'item':ItemCustomSelect(
                attrs={
                    'wrapper_class':'col-sm-4',
                    'data-item-select':True,
                }
            ),
            'porcentaje_impuesto':widgets.NumberInput(
                attrs={
                    'class':'text-right item-porcentaje-impuesto',
                }
            ),
            'precio':widgets.NumberInput(
                attrs={
                    'class':'text-right item-precio',
                }
            ),
            'cantidad':widgets.NumberInput(
                attrs={
                    'wrapper_class':'col-sm-1',
                }
            ),
        }

    }
    fields = ['item', 'cantidad','precio','porcentaje_impuesto',]
