from apps.inventory import models
from apps.inventory.forms import AjusteStockDetalleForm
from django import forms
from django.forms import widgets
from extra_views import InlineFormSetFactory


class AjusteStockDetalleInline(InlineFormSetFactory):
    model = models.AjusteStockDetalle
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
