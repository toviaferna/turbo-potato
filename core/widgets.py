from calculation import widgets
from dal_select2 import widgets as dal_widgets
from django import forms
from django.conf import settings
from django.utils import formats
from django.utils.formats import get_format

from core.mixins import MaskInputMixin, Select2WidgetMixin


class ModelSelect2(dal_widgets.QuerySetSelectMixin,
                   Select2WidgetMixin,
                   forms.Select):
   """"""

class AutocompleteSelect(ModelSelect2):

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs.setdefault('data-theme', 'bootstrap4')
        attrs.setdefault('data-html',True)
        attrs.setdefault('data-width','100%')
        return attrs




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
        'groupSeparator': get_format('THOUSAND_SEPARATOR'),
        'radixPoint': get_format('DECIMAL_SEPARATOR'),
    }



class DecimalField(forms.DecimalField):
    
    def __init__(self, max_digits=10, decimal_places=2, *args, **kwargs):
        self.widget = DecimalMaskInput()
        super(DecimalField, self).__init__(*args, **kwargs)
        self.widget.max_digits = max_digits
        self.widget.decimal_places = decimal_places
        self.localize = True

    def to_python(self, value):
        old_settings = settings.USE_L10N, settings.USE_THOUSAND_SEPARATOR

        settings.USE_L10N = True
        settings.USE_THOUSAND_SEPARATOR = True
        result = super().to_python(value)
         # restore original values
        settings.USE_L10N, settings.USE_THOUSAND_SEPARATOR = old_settings
        return result

class InvoiceNumberMaskInput(forms.CharField):
    widget = MaskInput(mask={'mask': '999-999-9999999'})

class SumInput(widgets.SumInput):
    #widget=DecimalMaskInput
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {
            'readonly':True, 
            'class':'text-danger text-right bg-white border-0 p-0' 
        }
        super().__init__(*args, **kwargs)
