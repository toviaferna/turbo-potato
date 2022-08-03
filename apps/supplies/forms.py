from apps.inventory.models import Deposito, Item
from apps.supplies import models
from core.layouts import FormActions, Formset
from core.widgets import (AutocompleteSelect, DateInput, FormulaInput,
                          InvoiceNumberMaskInput, ItemCustomSelect, SumInput)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Fieldset, Layout, Row
from django import forms
from django.forms.models import ModelForm


class PedidoCompraDetalleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["item"].queryset = Item.objects.filter(
            tipo_item__pk=2
        )  # sea igual a normal

    class Meta:
        model = models.PedidoCompraDetalle
        fields = ["item", "cantidad"]
        widgets = {
            "item": forms.Select(
                attrs={
                    "wrapper_class": "col-sm-10",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "wrapper_class": "col-sm-2",
                    "class": "text-right",
                }
            ),
        }


class PedidoCompraForm(forms.ModelForm):
    cantidad = forms.DecimalField(
        widget=SumInput("cantidad"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["cantidad"].label = False
        self.helper.layout = Layout(
            Row(
                Column("proveedor", css_class="col-sm-6"),
                Column("fecha_documento", css_class="col-sm-3"),
                Column("fecha_vencimiento", css_class="col-sm-3"),
            ),
            "observacion",
            Fieldset(
                "Detalle",
                Formset("PedidoCompraDetalleInline"),  # , stacked=True
            ),
            Row(
                Column(HTML("<label>Total</label>"), css_class="text-right col-sm-9"),
                Column(
                    "cantidad",
                    css_class="col-sm-2",
                ),
                Column(css_class="col-sm-1"),
            ),
            FormActions(),
        )

    class Meta:
        model = models.PedidoCompra
        fields = ["proveedor", "fecha_documento", "fecha_vencimiento", "observacion"]
        widgets = {
            "fecha_documento": DateInput,
            "fecha_vencimiento": DateInput,
            "proveedor": AutocompleteSelect(
                url="proveedor_autocomplete",
                attrs={
                    "data-placeholder": "Buscar por razon social, número de documento.",
                },
            ),
        }


class OrdenCompraDetalleForm(forms.ModelForm):

    subtotal = forms.DecimalField(
        widget=FormulaInput("(cantidad*(precio-descuento))", attrs={"readonly": True}),
        label="SubTotal",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["item"].queryset = Item.objects.filter(
            tipo_item__pk=2
        )  # sea igual a normal

    class Meta:
        model = models.OrdenCompraDetalle
        fields = ["item", "cantidad", "precio", "descuento"]
        widgets = {
            "item": forms.Select(
                attrs={
                    "wrapper_class": "col-sm-4",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "wrapper_class": "col-sm-1",
                    "class": "text-right",
                }
            ),
        }


class OrdenCompraForm(forms.ModelForm):
    total = forms.DecimalField(
        widget=SumInput(
            "subtotal",
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["total"].label = False
        self.helper.layout = Layout(
            Row(
                Column("pedido_compra", css_class="col-sm-5"),
                Column("proveedor", css_class="col-sm-5"),
                Column("fecha_documento", css_class="col-sm-2"),
            ),
            "observacion",
            Fieldset(
                "Detalle",
                Formset("OrdenCompraDetalleInline"),  # , stacked=True
            ),
            Row(
                Column(
                    HTML("<label> Total: </label>"),
                    css_class="text-right col-sm-9 mt-2",
                ),
                Column("total", css_class="col-sm-2"),
                Column(css_class="col-sm-1"),
            ),
            FormActions(),
        )

    class Meta:
        model = models.OrdenCompra
        fields = ["pedido_compra", "proveedor", "fecha_documento", "observacion"]
        widgets = {
            "fecha_documento": DateInput,
            "proveedor": AutocompleteSelect(
                url="proveedor_autocomplete",
            ),
        }


class CompraForm(forms.ModelForm):

    total = forms.DecimalField(
        widget=SumInput("subtotal"),
    )
    total_iva = forms.DecimalField(
        widget=SumInput("impuesto"),
    )

    comprobante = InvoiceNumberMaskInput()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["deposito"].queryset = Deposito.objects.filter(
            es_planta_acopiadora=False
        )
        self.fields["total"].label = False
        self.fields["total_iva"].label = False
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-3"),
                Column("comprobante"),
                Column("timbrado"),
                Column("es_credito", css_class="col-sm-3"),
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
                "Detalle",
                Formset(
                    "CompraDetalleInline",  # , stacked=True
                    css_class="compra-detalle-container",
                ),
                Formset("CuotaCompraInline", stacked=True, stacked_class="col-sm-3"),
            ),
            Row(
                Column(
                    HTML("<label> Total: </label>"),
                    css_class="text-right col-sm-9 mt-2",
                ),
                Column("total", css_class="col-sm-2"),
            ),
            Row(
                Column(
                    HTML("<label> Total Impuesto: </label>"),
                    css_class="text-right col-sm-9 mt-2",
                ),
                Column("total_iva", css_class="col-sm-2"),
            ),
            FormActions(),
        )

    class Meta:
        model = models.Compra
        fields = [
            "fecha_documento",
            "es_credito",
            "comprobante",
            "timbrado",
            "proveedor",
            "cuenta",
            "deposito",
            "observacion",
        ]
        widgets = {
            "fecha_documento": DateInput,
            "proveedor": AutocompleteSelect(
                url="proveedor_autocomplete",
            ),
        }


class CompraDetalleForm(forms.ModelForm):
    subtotal = forms.DecimalField(
        widget=FormulaInput("cantidad*costo"), label="SubTotal"
    )
    impuesto = forms.DecimalField(
        widget=FormulaInput(
            "parseFloat((subtotal*porcentaje_impuesto)/(porcentaje_impuesto+100)).toFixed(0)"
        ),
        label="Impuesto",
    )
    item = ItemCustomSelect()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["item"].queryset = Item.objects.filter(
            tipo_item__pk=2
        )  # sea igual a normal

    class Meta:
        model = models.CompraDetalle
        fields = [
            "item",
            "cantidad",
            "costo",
            "porcentaje_impuesto",
            "impuesto",
            "subtotal",
        ]


class CuotaCompraForm(forms.ModelForm):
    class Meta:
        model = models.CuotaCompra
        fields = ["fecha_vencimiento", "monto"]
        widgets = {
            "fecha_vencimiento": DateInput,
        }


class NotaDebitoRecibidaForm(forms.ModelForm):
    total = forms.DecimalField(
        widget=SumInput("subtotal"),
    )
    total_iva = forms.DecimalField(
        widget=SumInput("impuesto"),
    )
    comprobante = InvoiceNumberMaskInput()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["total"].label = False
        self.fields["total_iva"].label = False
        self.fields["compra"].queryset = models.Compra.objects.filter(es_vigente=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-3"),
                Column("comprobante"),
                Column("timbrado"),
                Column("es_credito", css_class="col-sm-3"),
            ),
            Row(
                Column("proveedor", css_class="col-sm-6"),
                Column("cuenta"),
                Column("deposito"),
            ),
            Row(Column("compra"), Column("observacion")),
            Fieldset(
                "Detalles",
                Formset("NotaDebitoRecibidaDetalleInline"),  # , stacked=True
            ),
            Row(
                Column(
                    HTML("<label> Total: </label>"),
                    css_class="text-right col-sm-9 mt-2",
                ),
                Column("total", css_class="col-sm-2"),
            ),
            Row(
                Column(
                    HTML("<label> Total impuesto: </label>"),
                    css_class="text-right col-sm-9 mt-2",
                ),
                Column("total_iva", css_class="col-sm-2"),
            ),
            FormActions(),
        )

    class Meta:
        model = models.NotaDebitoRecibida
        fields = [
            "fecha_documento",
            "es_credito",
            "comprobante",
            "timbrado",
            "proveedor",
            "cuenta",
            "deposito",
            "compra",
            "observacion",
        ]
        widgets = {
            "fecha_documento": DateInput,
            "proveedor": AutocompleteSelect(
                url="proveedor_autocomplete",
            ),
        }


class NotaDebitoRecibidaDetalleForm(forms.ModelForm):
    subtotal = forms.DecimalField(
        widget=FormulaInput("valor*cantidad"), label="SubTotal"
    )
    impuesto = forms.DecimalField(
        widget=FormulaInput(
            "parseFloat((subtotal*porcentaje_impuesto)/(porcentaje_impuesto+100)).toFixed(0)"
        ),
        label="Impuesto",
    )
    item = ItemCustomSelect()

    class Meta:
        model = models.NotaDebitoRecibidaDetalle
        fields = [
            "item",
            "cantidad",
            "valor",
            "porcentaje_impuesto",
            "impuesto",
            "subtotal",
        ]


class NotaCreditoRecibidaForm(forms.ModelForm):
    total = forms.DecimalField(
        widget=SumInput("subtotal"),
    )
    total_iva = forms.DecimalField(
        widget=SumInput("impuesto"),
    )
    comprobante = InvoiceNumberMaskInput()

    class Meta:
        model = models.NotaCreditoRecibida
        fields = [
            "fecha_documento",
            "es_credito",
            "comprobante",
            "timbrado",
            "proveedor",
            "cuenta",
            "deposito",
            "compra",
            "observacion",
        ]
        widgets = {
            "fecha_documento": DateInput,
            "proveedor": AutocompleteSelect(
                url="proveedor_autocomplete",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["total"].label = False
        self.fields["total_iva"].label = False
        self.fields["compra"].queryset = models.Compra.objects.filter(es_vigente=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-3"),
                Column("comprobante"),
                Column("timbrado"),
                Column("es_credito", css_class="col-sm-3"),
            ),
            Row(Column("proveedor"), Column("cuenta"), Column("deposito")),
            Row(Column("compra"), Column("observacion")),
            Fieldset(
                "Detalles",
                Formset("NotaCreditoRecibidaDetalleInline"),
            ),
            Row(
                Column(
                    HTML("<label> Total: </label>"),
                    css_class="text-right col-sm-9 mt-2",
                ),
                Column("total", css_class="col-sm-2"),
            ),
            Row(
                Column(
                    HTML("<label> Total impuesto: </label>"),
                    css_class="text-right col-sm-9 mt-2",
                ),
                Column("total_iva", css_class="col-sm-2"),
            ),
            FormActions(),
        )


class NotaCreditoRecibidaDetalleForm(forms.ModelForm):
    subtotal = forms.DecimalField(
        widget=FormulaInput("valor*cantidad"), label="SubTotal"
    )
    impuesto = forms.DecimalField(
        widget=FormulaInput(
            "parseFloat((subtotal*porcentaje_impuesto)/(porcentaje_impuesto+100)).toFixed(0)"
        ),
        label="Impuesto",
    )
    item = ItemCustomSelect()

    class Meta:
        model = models.NotaCreditoRecibidaDetalle
        fields = [
            "es_devolucion",
            "item",
            "cantidad",
            "valor",
            "porcentaje_impuesto",
            "impuesto",
            "subtotal",
        ]
