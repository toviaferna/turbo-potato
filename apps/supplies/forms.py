from django import forms
from django.forms.models import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder,Layout, Submit, Row, Column,Fieldset, HTML, Div,Field
from apps.inventory.models import Item
from apps.supplies.models import OrdenCompra, OrdenCompraDetalle, PedidoCompra, PedidoCompraDetalle
from core.layouts import Formset
from apps.finance.models import Persona
import calculation
from core.widgets import DateInput, SumInput
from core.layouts import CancelButton 

class PedidoCompraDetalleForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["item"].queryset = Item.objects.filter(tipo_item__pk=2) # sea igual a normal
    
    class Meta:
        model = PedidoCompraDetalle
        fields = ['item', 'cantidad']
        widgets = {
            'item':forms.Select(
                attrs={
                    'wrapper_class':'col-sm-10',
                }
            ),
            'cantidad':forms.NumberInput(
                attrs={
                    'wrapper_class':'col-sm-2',
                    'class':'text-right',
                }
            ),
        }

class PedidoCompraForm(forms.ModelForm):
    cantidad = forms.DecimalField(
        widget=SumInput('cantidad'),
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
                Column("proveedor", css_class="col-sm-6"),
                Column("fecha_documento", css_class="col-sm-3"),
                Column("fecha_vencimiento", css_class="col-sm-3")
            ),
            "observacion",
            Fieldset(
                u'Detalle',
                Formset(
                    "PedidoCompraDetalleInline"#, stacked=True
                ), 
            ),

            Row(
                Column(HTML("<label>Total</label>"),css_class="text-right col-sm-9"), 
                Column("cantidad", css_class="col-sm-2",),
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

class OrdenCompraDetalleForm(forms.ModelForm):
    subtotal = forms.DecimalField(
        widget=calculation.FormulaInput('(cantidad*(precio-descuento))', attrs={'readonly':True}),
        label = "SubTotal"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["item"].queryset =  Item.objects.filter(tipoItem__pk=2) # sea igual a normal
    class Meta:
        model = OrdenCompraDetalle
        fields = ['item', 'cantidad','precio','descuento']
        widgets = {
            'item':forms.Select(
                attrs={
                    'wrapper_class':'col-sm-4',
                }
            ),
            'cantidad':forms.NumberInput(
                attrs={
                    'wrapper_class':'col-sm-1',
                    'class':'text-right',
                }
            ),
        }

class OrdenCompraForm(forms.ModelForm):
    total = forms.DecimalField(
        widget=SumInput('subtotal',),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["proveedor"].queryset =  proveedor = Persona.objects.filter(esProveedor=True)
        self.fields['total'].label = False
        #self.fields['total'].widget = DecimalMaskInput()
        self.helper.layout = Layout(
            "pedido_compra",
            "proveedor",
            "fecha_documento",
            "observacion",
            Fieldset(
                u'Detalle',
                Formset(
                    "OrdenCompraDetalleInline"#, stacked=True
                ), 
                
            ),
             Row(
                #Column(
 
                Column( HTML('<label> Total: </label>'),css_class='text-right col-sm-10 mt-2'),
                Column("total", css_class='col')
            ), 
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            )
        )
    class Meta:
        model = OrdenCompra
        fields = ['pedido_compra','proveedor','fecha_documento', 'observacion']
        widgets = {'fecha_documento':DateInput}