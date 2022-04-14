from apps.finance.models import Persona
from apps.inventory.models import Deposito, Item
from apps.supplies.models import (Compra, CompraDetalle, CuotaCompra, NotaDebitoRecibida, NotaDebitoRecibidaDetalle, OrdenCompra, OrdenCompraDetalle,
                                  PedidoCompra, PedidoCompraDetalle)
from core.layouts import CancelButton, Formset, SaveButton
from core.widgets import DateInput, FormulaInput, ItemCustomSelect, SumInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, ButtonHolder, Column,
                                 Fieldset, Layout, Row, Submit)
from django import forms
from django.forms.models import ModelForm


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
                SaveButton(),
                CancelButton(),
            )
        )
    class Meta:
        model = PedidoCompra
        fields = ['proveedor','fecha_documento', 'fecha_vencimiento', 'observacion']
        widgets = {'fecha_documento':DateInput,'fecha_vencimiento':DateInput}

class OrdenCompraDetalleForm(forms.ModelForm):
    subtotal = forms.DecimalField(
        widget=FormulaInput('(cantidad*(precio-descuento))', attrs={'readonly':True}),
        label = "SubTotal"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["item"].queryset = Item.objects.filter(tipo_item__pk=2) # sea igual a normal
    
    class Meta:
        model = OrdenCompraDetalle
        fields = ['item','cantidad','precio','descuento']
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
        self.fields["proveedor"].queryset = Persona.objects.filter(es_proveedor=True)
        self.fields['total'].label = False
        #self.fields['total'].widget = DecimalMaskInput()
        self.helper.layout = Layout(
            Row(
                Column("pedido_compra", css_class="col-sm-5"),
                Column("proveedor", css_class="col-sm-5"),
                Column("fecha_documento", css_class="col-sm-2"),
            ),
            "observacion",
            Fieldset(
                u'Detalle',
                Formset(
                    "OrdenCompraDetalleInline"#, stacked=True
                ), 
                
            ),
             Row(
                Column(HTML('<label> Total: </label>'),css_class='text-right col-sm-9 mt-2'),
                Column("total", css_class='col-sm-2'),
                Column(css_class='col-sm-1')
            ), 
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            )
        )
    class Meta:
        model = OrdenCompra
        fields = ['pedido_compra','proveedor','fecha_documento', 'observacion']
        widgets = {'fecha_documento':DateInput}


class CompraForm(forms.ModelForm):
    total = forms.DecimalField(
        widget=SumInput('subtotal'),
    )
    total_iva = forms.DecimalField(
        widget=SumInput('impuesto'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["proveedor"].queryset =  Persona.objects.filter(es_proveedor=True)
        self.fields["deposito"].queryset = Deposito.objects.filter(es_planta_acopiadora=False)
        self.fields['total'].label = False
        #self.fields['total'].widget = DecimalMaskInput()
        self.fields['total_iva'].label = False
        #self.fields['total_iva'].widget = DecimalMaskInput()
        #self.fields['comprobante'].widget = InvoiceMaskInput()
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-3"),
                Column("comprobante"),
                Column("timbrado"),
                Column("es_credito", css_class="col-sm-3 mt-2"),
            ),
            Row(
                Column("proveedor"),
                Column("cuenta"),
            ),
            Row(
                Column("deposito"),
                Column("observacion"),
            ),
            Fieldset(
                u'Detalle',
                Formset(
                    "CompraDetalleInline",#, stacked=True
                    css_class="compra-detalle-container"
                ),  
                Formset(
                    "CuotaCompraInline",
                    stacked=True,
                    stacked_class="col-sm-3"
                ), 
            ),
            Row(
                Column(
                    HTML('<label> Total: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total", css_class="col-sm-2")
            ),
            Row(
                Column(
                    HTML('<label> Total Impuesto: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total_iva", css_class="col-sm-2")
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            )
        )
    class Meta:
        model = Compra
        fields = ['fecha_documento','es_credito','comprobante', 'timbrado','proveedor','cuenta','deposito','observacion']
        widgets = {'fecha_documento':DateInput}

class CompraDetalleForm(forms.ModelForm):
    subtotal = forms.DecimalField(
        widget=FormulaInput('cantidad*costo'),
        label = "SubTotal"
    )
    impuesto = forms.DecimalField(
        widget=FormulaInput('parseFloat((subtotal*porcentaje_impuesto)/(porcentaje_impuesto+100)).toFixed(0)'),
        label = "Impuesto"
    )
    item = ItemCustomSelect()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["item"].queryset =  item = Item.objects.filter(tipo_item__pk=2) # sea igual a normal
    class Meta:
        model = CompraDetalle
        fields = ['item', 'cantidad','costo','porcentaje_impuesto','impuesto','subtotal']
        #widgets = {'costo':DecimalMaskInput,'cantidad':DecimalMaskInput,'porcentajeImpuesto':DecimalMaskInput,'impuesto':DecimalMaskInput,'subtotal':DecimalMaskInput}

class CuotaCompraForm(forms.ModelForm):
    class Meta:
        model = CuotaCompra
        fields = ['fecha_vencimiento','monto']
        widgets = { 'fecha_vencimiento':DateInput, } #'monto':DecimalMaskInput }

class NotaDebitoRecibidaForm(forms.ModelForm):
    total = forms.DecimalField(
        widget=SumInput('subtotal'),
    )
    total_iva = forms.DecimalField(
        widget=SumInput('impuesto'),
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['total'].label = False
        #self.fields['total'].widget = DecimalMaskInput()
        self.fields['total_iva'].label = False
        #self.fields['total_iva'].widget = DecimalMaskInput()
        #self.fields['comprobante'].widget = InvoiceMaskInput()
        self.fields["proveedor"].queryset =  proveedor = Persona.objects.filter(es_proveedor=True)
        self.fields["compra"].queryset =  compra = Compra.objects.filter(es_vigente=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-3"),
                Column("comprobante"),
                Column("timbrado"),
                Column("es_credito", css_class="col-sm-3 mt-2"),
            ),
            Row(
                Column("proveedor", css_class="col-sm-6"),
                Column("cuenta"),
                Column("deposito")
            ),
            Row(
                Column("compra"),
                Column("observacion")
            ),
            Fieldset(
                u'Detalles',
                Formset(
                    "NotaDebitoRecibidaDetalleInline"#, stacked=True
                ), 
                
            ),
            Row(
                Column(
                    HTML('<label> Total: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total", css_class="col-sm-2")
            ),
            Row(
                Column(
                    HTML('<label> Total impuesto: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total_iva", css_class="col-sm-2")
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton()
            )
        )
    class Meta:
        model = NotaDebitoRecibida
        fields = ['fecha_documento','es_credito','comprobante','timbrado','proveedor','cuenta','deposito',"compra",'observacion']
        widgets = {'fecha_documento':DateInput}

class NotaDebitoRecibidaDetalleForm(forms.ModelForm):
    subtotal = forms.DecimalField(
        widget=FormulaInput('valor*cantidad'),
        label = "SubTotal"
    )
    impuesto = forms.DecimalField(
        widget=FormulaInput('parseFloat((subtotal*porcentaje_impuesto)/(porcentaje_impuesto+100)).toFixed(0)'),
        label = "Impuesto"
    )
    item = ItemCustomSelect()
    class Meta:
        model = NotaDebitoRecibidaDetalle
        fields = ['item', 'cantidad','valor','porcentaje_impuesto','impuesto','subtotal']
        #widgets = {'cantidad':DecimalMaskInput,'valor':DecimalMaskInput,'porcentajeImpuesto':DecimalMaskInput,'impuesto':DecimalMaskInput,'subtotal':DecimalMaskInput}