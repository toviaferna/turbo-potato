from django import forms
from django.forms.models import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder,Layout, Submit, Row, Column,Fieldset, HTML, Div,Field
from apps.inventory.models import Item
from apps.supplies.models import PedidoCompra, PedidoCompraDetalle
from core.layouts import Formset
from apps.finance.models import Persona
import calculation
from core.widgets import DateInput
from core.layouts import CancelButton 

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
                Column("proveedor", css_class="col-sm-8"),
                Column("fecha_documento", css_class="col-sm-2"),
                Column("fecha_vencimiento", css_class="col-sm-2")
            ),
            "observacion",
            Fieldset(
                u'Detalle',
                Formset(
                    "PedidoCompraDetalleInline"#, stacked=True
                ), 
                
            ),

            Row(
                Column(HTML("<label>Cantidad</label> {{cantidad}}"),css_class="text-right col-sm-9"), 
                Column(Field("cantidad", css_class="text-danger text-right bg-white border-0"), css_class="col-sm-2",),
                Column(css_class="col-sm-1"),
            ),
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            )
        )
    class Meta:
        model = PedidoCompra
        fields = ['proveedor','fecha_documento', 'fecha_vencimiento', 'observacion']
        widgets = {'fecha_documento':DateInput,'fecha_vencimiento':DateInput}