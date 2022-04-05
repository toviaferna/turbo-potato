from extra_views import InlineFormSetFactory
from apps.inventory.forms import AjusteStockDetalleForm

from apps.inventory.models import AjusteStockDetalle
from django import forms
from django.forms import widgets

class AjusteStockDetalleInline(InlineFormSetFactory):
    model = AjusteStockDetalle
    form_class = AjusteStockDetalleForm
    factory_kwargs = {
        'extra':1 ,
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
    fields = ['item', 'cantidad',]