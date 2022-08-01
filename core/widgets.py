from calculation import widgets
from django import forms

from core.mixins import MaskInputMixin


class DateInput(forms.DateInput):
    input_type = 'date'
    def __init__(self, attrs=None, format=None):
        super().__init__(attrs, format='%Y-%m-%d' if format is None else format)

class FormulaInput(widgets.FormulaInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {
            'readonly':True,
            'class':'text-right'
        }
        super().__init__(*args, **kwargs)

class ItemCustomSelect(forms.Select):

    def __init__(self, attrs=None, choices=(), modify_choices=()):
        super().__init__(attrs, choices=choices)
        self.modify_choices = modify_choices

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)

        if value:
            option['attrs']['data-precio'] = value.instance.precio
            option['attrs']['data-costo'] = value.instance.costo
            option['attrs']['data-ultimo-costo'] = value.instance.ultimo_costo
            option['attrs']['data-tipo-impuesto-id'] = value.instance.tipo_impuesto.id
            option['attrs']['data-tipo-impuesto-descripcion'] = value.instance.tipo_impuesto.descripcion
            option['attrs']['data-tipo-impuesto-porcentaje'] = value.instance.tipo_impuesto.porcentaje
            option['attrs']['data-tipo-impuesto-iva'] = value.instance.tipo_impuesto.es_iva

        return option

class MaquinariaCustomSelect(forms.Select):
    
    def __init__(self, attrs=None, choices=(), modify_choices=()):
        super().__init__(attrs, choices=choices)
        # set data
        self.modify_choices = modify_choices

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['data-precio-ha'] = value.instance.precio

        return option

class MaskInput(MaskInputMixin, forms.TextInput):
    """"""

class DecimalMaskInput(MaskInputMixin, forms.TextInput):

    mask = {
        'alias': 'decimal',
        'step': 0,
        'autoUnmask': True,
        'unmaskAsNumber': True,
        'clearMaskOnLostFocus': False,
        #'groupSeparator': ','
    }

class DecimalField(forms.DecimalField):
    widget = DecimalMaskInput

class InvoiceNumberMaskInput(forms.CharField):
    widget = MaskInput(mask={'mask': '999-999-9999999'})

class SumInput(widgets.SumInput):
    widget=DecimalMaskInput
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {
            'readonly':True, 
            'class':'text-danger text-right bg-white border-0 p-0' 
        }
        super().__init__(*args, **kwargs)
