


from apps.finance.models import Persona
from apps.sales import models
from core import widgets
from core.layouts import CancelButton, FormActions, Formset, SaveButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, ButtonHolder, Column, Fieldset, Layout,
                                 Row)
from django.forms import DecimalField, ModelForm


class AperturaCajaCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("empleado"),
                Column("monto_inicio", css_class="col-sm-3"),
                
            ),
            Row(
               Column("observacion",),
            ),
            
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.AperturaCaja
        fields = ["empleado","observacion","monto_inicio",]


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
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.Arqueo
        fields = ['empleado','apertura_caja','observacion','monto']

class TransferenciaCuentaForm(ModelForm):
    class Meta:
        model = models.TransferenciaCuenta
        fields = ['fecha','comprobante','cuenta_salida','cuenta_entrada','monto','observacion']
        widgets = {'fecha':widgets.DateInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column("fecha", css_class="col-sm-3"),
                Column("comprobante", css_class="col-sm-3"),
                Column("cuenta_salida",),
            ),
            Row(
                Column("cuenta_entrada",),
                Column("monto", css_class="col-sm-3"),
            ),
            "observacion",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )

class CuotaVentaForm(ModelForm):
    class Meta:
        model = models.CuotaVenta
        fields = ['fecha_vencimiento','monto']
        widgets = { 'fecha_vencimiento':widgets.DateInput }

class VentaDetalleForm(ModelForm):
    subtotal = DecimalField(
        widget=widgets.FormulaInput('precio*cantidad'),
        label = "Subtotal"
    )
    impuesto = DecimalField(
        widget=widgets.FormulaInput('parseFloat((subtotal*porcentaje_impuesto)/(porcentaje_impuesto+100)).toFixed(0)'),
        label = "Impuesto"
    )
    class Meta:
        model = models.VentaDetalle 
        fields = ['item', 'cantidad','precio','porcentaje_impuesto','impuesto','subtotal']
        #widgets = {'cantidad':DecimalMaskInput,'precio':DecimalMaskInput,'porcentaje_impuesto':DecimalMaskInput,'impuesto':DecimalMaskInput,'subtotal':DecimalMaskInput}

class VentaForm(ModelForm):
    total = DecimalField(
        widget=widgets.SumInput('subtotal'),
    )
    total_iva = DecimalField(
        widget=widgets.SumInput('impuesto'),
    )
    class Meta:
        model = models.Venta
        fields = ['fecha_documento','es_credito','comprobante','cliente','cuenta','deposito','observacion']
        widgets = {'fecha_documento':widgets.DateInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['total'].label = False
        #self.fields['total'].widget = DecimalMaskInput()
        self.fields['total_iva'].label = False
        #self.fields['total_iva'].widget = DecimalMaskInput()
        #self.fields['comprobante'].widget = InvoiceMaskInput()
        self.fields["cliente"].queryset = Persona.objects.filter(es_cliente=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-2"),
                Column("comprobante",css_class="col-sm-2"),
                Column("cliente",),
                Column("es_credito",css_class="col-sm-2"),
            ),
            Row(
                Column("cuenta",),
                Column("deposito",),
                Column("observacion",),
            ),
            
            Fieldset(
                u'Detalles',
                Formset(
                    "VentaDetalleInline"
                ), 
                Formset(
                    "CuotaVentaInline",
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
            Row(
                Column(
                    HTML("<label> Total impuesto: </label>"),
                    css_class="text-right col-sm-9 mt-2",
                ),
                Column("total_iva", css_class="col-sm-2"),
            ),
            FormActions()
        )
