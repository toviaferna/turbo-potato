from django import forms
from django.forms.models import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder,Layout, Submit, Row, Column,Fieldset, HTML, Div
from apps.inventory.models import Item
from apps.supplies.models import PedidoCompra, PedidoCompraDetalle
from core.layouts import Formset
from apps.finance.models import Persona
import calculation
from core.widgets import DateInput
class PedidoCompraDetalleForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["item"].queryset =  item = Item.objects.filter(tipo_item__pk=2) # sea igual a normal
    class Meta:
        model = PedidoCompraDetalle
        fields = ['item', 'cantidad']
        #widgets = {'cantidad':DecimalMaskInput}

class PedidoCompraForm(forms.ModelForm):
    cantidad = forms.DecimalField(
        widget=calculation.SumInput('cantidad',   attrs={'readonly':True}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['cantidad'].label = False
        #self.fields['cantidad'].widget = DecimalMaskInput()
        self.fields["proveedor"].queryset =  proveedor = Persona.objects.filter(es_proveedor=True)
        self.helper.layout = Layout(
            Row(
                Column("proveedor"),
                Column("fecha_documento"),
                Column("fecha_vencimiento")
            ),
            "observacion",
            Fieldset(
                u'Detalle',
                Formset(
                    "PedidoCompraDetalleInline"#, stacked=True
                ), 
                
            ),
            Row(
                Column(
                    HTML("<div class='w-100'></div>")
                ), 
                Column(
                    HTML('<span class="w-100"> Cantidad: </span>'),
                    css_class="text-right"
                ), 
                Column("cantidad", css_class="col-sm-3")
            ),  
            Row(
                Div(
                    Submit("submit", "Guardar",css_class = "btn btn-success"), 
                    HTML("""<a class="btn btn-secondary" href="{% url 'pedido_compra_list' %}"> Cancelar</a>""" )
                )
            ) ,
        )
    class Meta:
        model = PedidoCompra
        fields = ['proveedor','fecha_documento', 'fecha_vencimiento', 'observacion']
        widgets = {'fecha_documento':DateInput,'fecha_vencimiento':DateInput}