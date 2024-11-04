from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Fieldset, Layout, Row
from django import forms
from django.forms import (BooleanField, CharField, DecimalField, HiddenInput,
                          ModelForm)

from apps.finance.models import Persona
from apps.sales import models
from core import widgets
from core.layouts import FormActions, Formset


class AperturaCajaCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["empleado"].queryset = Persona.objects.filter(es_empleado=True)
        self.helper.layout = Layout(
            Row(
                Column("empleado"),
                Column("monto_inicio", css_class="col-sm-3"),
            ),
            Row(
                Column(
                    "observacion",
                ),
            ),
            FormActions(),
        )

    class Meta:
        model = models.AperturaCaja
        fields = [
            "empleado",
            "observacion",
            "monto_inicio",
        ]


class ArqueoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["empleado"].queryset = Persona.objects.filter(es_empleado=True)
        self.helper.layout = Layout(
            Row(
                Column("empleado"),
                Column("apertura_caja"),
            ),
            Row(
                Column("observacion"),
                Column("monto", css_class="col-sm-3"),
            ),
            FormActions(),
        )

    class Meta:
        model = models.Arqueo
        fields = ["empleado", "apertura_caja", "observacion", "monto"]


class TransferenciaCuentaForm(ModelForm):
    class Meta:
        model = models.TransferenciaCuenta
        fields = [
            "fecha",
            "comprobante",
            "cuenta_salida",
            "cuenta_entrada",
            "monto",
            "observacion",
        ]
        widgets = {"fecha": widgets.DateInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column("fecha", css_class="col-sm-3"),
                Column("comprobante", css_class="col-sm-3"),
                Column(
                    "cuenta_salida",
                ),
            ),
            Row(
                Column(
                    "cuenta_entrada",
                ),
                Column("monto", css_class="col-sm-3"),
            ),
            "observacion",
            FormActions(),
        )


class CuotaVentaForm(ModelForm):
    class Meta:
        model = models.CuotaVenta
        fields = ["fecha_vencimiento", "monto"]
        widgets = {"fecha_vencimiento": widgets.DateInput}


class VentaDetalleForm(ModelForm):
    subtotal = DecimalField(
        widget=widgets.FormulaInput("precio*cantidad"), label="Subtotal"
    )
    impuesto = DecimalField(
        widget=widgets.FormulaInput(
            "parseFloat((subtotal*porcentaje_impuesto)/(porcentaje_impuesto+100)).toFixed(0)"
        ),
        label="Impuesto",
    )

    class Meta:
        model = models.VentaDetalle
        fields = [
            "item",
            "cantidad",
            "precio",
            "porcentaje_impuesto",
            "impuesto",
            "subtotal",
        ]
        # widgets = {'cantidad':DecimalMaskInput,'precio':DecimalMaskInput,'porcentaje_impuesto':DecimalMaskInput,'impuesto':DecimalMaskInput,'subtotal':DecimalMaskInput}


class VentaForm(ModelForm):
    total = DecimalField(
        widget=widgets.SumInput("subtotal"),
    )
    total_iva = DecimalField(
        widget=widgets.SumInput("impuesto"),
    )
    comprobante = widgets.InvoiceNumberMaskInput()

    class Meta:
        model = models.Venta
        fields = [
            "fecha_documento",
            "es_credito",
            "comprobante",
            "cliente",
            "cuenta",
            "deposito",
            "observacion",
        ]
        widgets = {
            "fecha_documento": widgets.DateInput,
            "cliente": widgets.AutocompleteSelect(
                url="cliente_autocomplete",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["total"].label = False
        # self.fields['total'].widget = DecimalMaskInput()
        self.fields["total_iva"].label = False
        # self.fields['total_iva'].widget = DecimalMaskInput()
        self.fields["cliente"].queryset = Persona.objects.filter(es_cliente=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-2"),
                Column("comprobante", css_class="col-sm-2"),
                Column(
                    "cliente",
                ),
                Column(
                    "es_credito",
                    css_class="col-sm-2",
                ),
            ),
            Row(
                Column(
                    "cuenta",
                ),
                Column(
                    "deposito",
                ),
                Column(
                    "observacion",
                ),
            ),
            Fieldset(
                "Detalles",
                Formset("VentaDetalleInline"),
                Formset("CuotaVentaInline", stacked=True, stacked_class="col-sm-3"),
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


class NotaCreditoEmitidaForm(ModelForm):
    total = DecimalField(
        widget=widgets.SumInput(
            "subtotal",
        ),
    )
    total_iva = DecimalField(
        widget=widgets.SumInput(
            "impuesto",
        ),
    )
    comprobante = widgets.InvoiceNumberMaskInput()

    class Meta:
        model = models.NotaCreditoEmitida
        fields = [
            "fecha_documento",
            "es_credito",
            "comprobante",
            #"timbrado",
            "cliente",
            "cuenta",
            "deposito",
            "venta",
            "observacion",
        ]
        widgets = {
            "fecha_documento": widgets.DateInput,
            "cliente": widgets.AutocompleteSelect(
                url="cliente_autocomplete",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["total"].label = False
        # self.fields['total'].widget = DecimalMaskInput()
        self.fields["total_iva"].label = False
        # self.fields['total_iva'].widget = DecimalMaskInput()
        self.fields["cliente"].queryset = Persona.objects.filter(es_cliente=True)
        self.fields["venta"].queryset = models.Venta.objects.filter(es_vigente=True)
        self.helper.layout = Layout(
            Row(
                Column(
                    "fecha_documento",
                ),
                Column(
                    "comprobante",
                ),
                Column(
                    "es_credito",
                ),
            ),
            Row(
                Column(
                    "cliente",
                ),
                Column(
                    "cuenta",
                ),
                Column(
                    "deposito",
                ),
            ),
            Row(
                Column("venta", css_class="col-sm-4"),
                Column(
                    "observacion",
                ),
            ),
            Fieldset(
                "Detalles",
                Formset("NotaCreditoEmitidaDetalleInline"),  # , stacked=True
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


class NotaCreditoEmitidaDetalleForm(ModelForm):
    subtotal = DecimalField(
        widget=widgets.FormulaInput("valor*cantidad"), label="SubTotal"
    )
    impuesto = DecimalField(
        widget=widgets.FormulaInput(
            "parseFloat((subtotal*porcentaje_impuesto)/(porcentaje_impuesto+100)).toFixed(0)",
        ),
        label="Impuesto",
    )

    class Meta:
        model = models.NotaCreditoEmitidaDetalle
        fields = [
            "es_devolucion",
            "item",
            "cantidad",
            "valor",
            "porcentaje_impuesto",
            "impuesto",
            "subtotal",
        ]
        # widgets = {'cantidad':DecimalMaskInput,'valor':DecimalMaskInput,'porcentajeImpuesto':DecimalMaskInput,'impuesto':DecimalMaskInput,'subtotal':DecimalMaskInput}


class NotaDebitoEmitidaForm(ModelForm):
    total = DecimalField(
        widget=widgets.SumInput(
            "subtotal",
        ),
    )
    total_iva = DecimalField(
        widget=widgets.SumInput(
            "impuesto",
        ),
    )
    comprobante = widgets.InvoiceNumberMaskInput()

    class Meta:
        model = models.NotaDebitoEmitida
        fields = [
            "fecha_documento",
            "es_credito",
            "comprobante",
            "cliente",
            "cuenta",
            "deposito",
            "venta",
            "observacion",
        ]
        widgets = {
            "fecha_documento": widgets.DateInput,
            "cliente": widgets.AutocompleteSelect(
                url="cliente_autocomplete",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["total"].label = False
        # self.fields['total'].widget = DecimalMaskInput()
        self.fields["total_iva"].label = False
        # self.fields['total_iva'].widget = DecimalMaskInput()
        # self.fields['comprobante'].widget = InvoiceMaskInput()
        self.fields["cliente"].queryset = Persona.objects.filter(es_cliente=True)
        self.fields["venta"].queryset = models.Venta.objects.filter(es_vigente=True)
        self.helper.layout = Layout(
            Row(
                Column(
                    "fecha_documento",
                ),
                Column(
                    "comprobante",
                ),
                Column(
                    "es_credito",
                ),
            ),
            Row(
                Column(
                    "cliente",
                ),
                Column(
                    "cuenta",
                ),
                Column(
                    "deposito",
                ),
            ),
            Row(
                Column("venta", css_class="col-sm-6"),
                Column(
                    "observacion",
                ),
            ),
            Fieldset(
                "Detalles",
                Formset("NotaDebitoEmitidaDetalleInline"),  # , stacked=True
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


class NotaDebitoEmitidaDetalleForm(ModelForm):
    subtotal = DecimalField(
        widget=widgets.FormulaInput(
            "valor*cantidad",
        ),
        label="SubTotal",
    )
    impuesto = DecimalField(
        widget=widgets.FormulaInput(
            "parseFloat((subtotal*porcentaje_impuesto)/(porcentaje_impuesto+100)).toFixed(0)",
        ),
        label="Impuesto",
    )

    class Meta:
        model = models.NotaDebitoEmitidaDetalle
        fields = [
            "item",
            "cantidad",
            "valor",
            "porcentaje_impuesto",
            "impuesto",
            "subtotal",
        ]
        # widgets = {'cantidad':DecimalMaskInput,'valor':DecimalMaskInput,'porcentajeImpuesto':DecimalMaskInput,'impuesto':DecimalMaskInput,'subtotal':DecimalMaskInput}


class CobroForm(ModelForm):

    total = DecimalField(
        widget=widgets.SumInput(
            "cancelacion",
        ),
    )

    class Meta:
        model = models.Cobro
        fields = [
            "fecha_documento",
            "comprobante",
            "cliente",
            "cuenta",
            "cobrador",
            "monto_a_saldar",
            "observacion",
        ]
        widgets = {
            "fecha_documento": widgets.DateInput,
        }  #'monto_a_saldar':DecimalMaskInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["total"].label = False
        # self.fields['total'].widget = DecimalMaskInput()
        # self.fields['comprobante'].widget = InvoiceMaskInput()
        self.fields["cliente"].queryset = Persona.objects.filter(es_cliente=True)
        self.fields["cobrador"].queryset = Persona.objects.filter(es_empleado=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-3"),
                Column("comprobante", css_class="col-sm-3"),
                Column(
                    "cliente",
                ),
            ),
            Row(
                Column(
                    "cobrador",
                ),
                Column(
                    "cuenta",
                ),
                Column("monto_a_saldar", css_class="col-sm-3"),
            ),
            "observacion",
            Fieldset(
                "Detalle",
                Formset("CobroDetalleInline"),  # , stacked=True
                Formset(
                    "CobroMedioInline",
                    stacked=True,
                ),
            ),
            Row(
                Column(
                    HTML("<label> Total: </label>"),
                    css_class="text-right col-sm-9 mt-2",
                ),
                Column("total", css_class="col-sm-2"),
            ),
            FormActions(),
        )


class CobroDetalleForm(ModelForm):
    check = BooleanField(label="Sel.", required=False)
    comprobante = CharField(max_length=30, disabled=True)
    monto = DecimalField(max_digits=15, disabled=True)
    saldo = DecimalField(max_digits=15, disabled=True)

    class Meta:
        model = models.CobroDetalle
        fields = ["cuota_venta", "check", "cancelacion"]
        widgets = {
            #'cancelacion':DecimalMaskInput,
            #'monto':DecimalMaskInput,
            #'saldo':DecimalMaskInput,
            "cuota_venta": HiddenInput
        }


class CobroMedioForm(ModelForm):
    class Meta:
        model = models.CobroMedio
        fields = ["numero", "comprobante", "medio_cobro", "observacion", "monto"]
        # widgets = {'cancelacion':DecimalMaskInput}

class TipoDocumentoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            FormActions()
        )
    class Meta:
        model = models.TipoDocumento
        fields = ["descripcion",]

class EstablecimientoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            FormActions()
        )
    class Meta:
        model = models.Establecimiento
        fields = ["descripcion",]

class PuntoExpedicionForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "establecimiento",
            "descripcion",
            FormActions()
        )
    class Meta:
        model = models.PuntoExpedicion
        fields = ["establecimiento", "descripcion",]

class TimbradoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("numero"),
                Column("tipo_documento"),
                Column("punto_expedicion"),
            ),
            Row(
                Column("inicio_vigencia"),
                Column("fin_vigencia"),
            ),
            Row(
                Column("numero_inicial"),
                Column("numero_final"),
                Column("es_vigente"),
            ),
            FormActions()
        )
    class Meta:
        model = models.Timbrado
        fields = ["numero","tipo_documento","punto_expedicion","inicio_vigencia","fin_vigencia","numero_inicial","numero_final","es_vigente",]
        widgets = {
            "inicio_vigencia": widgets.DateInput,
            "fin_vigencia": widgets.DateInput,
        }