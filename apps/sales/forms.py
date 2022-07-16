


from apps.finance.models import Persona
from apps.sales import models
from core import widgets
from core.layouts import CancelButton, SaveButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Layout, Row
from django.forms import ModelForm


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
