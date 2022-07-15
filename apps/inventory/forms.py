from apps.finance.models import Persona
from apps.inventory import models
from core.layouts import CancelButton, Formset, SaveButton
from core.widgets import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Fieldset, Layout, Row
from django.forms.models import ModelForm


class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.Marca
        fields = ['descripcion',]

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.Categoria
        fields = ['descripcion',]

class TipoItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.TipoItem
        fields = ['descripcion',]

class ItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("descripcion"),
                Column("codigo_barra"),
                Column("tipo_item"),
            ),
            Row(
                Column("categoria"),
                Column("marca"),
                Column("tipo_impuesto"),
            ),
            Row(
                Column("precio", css_class="col-sm-4"),
            ),
            "es_activo",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.Item
        fields = ['descripcion','codigo_barra','tipo_item','categoria','marca','tipo_impuesto','precio','es_activo']

class DepositoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "es_planta_acopiadora",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.Deposito
        fields = ['descripcion','es_planta_acopiadora']

class AjusteStockForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["empleado"].queryset =  Persona.objects.filter(es_empleado=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-3"),
                Column("comprobante", css_class="col-sm-3"),
                Column("empleado"),
            ),
            Row(
                Column("deposito", css_class="col-sm-4"),
                Column("observacion"),
            ),
            Fieldset(
                u'Detalles',
                Formset(
                    "AjusteStockDetalleInline"#, stacked=True
                ), 
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
       model = models.AjusteStock
       fields = ['fecha_documento','comprobante','empleado','deposito','observacion',]
       widgets = { 'fecha_documento':DateInput }

class AjusteStockDetalleForm(ModelForm):
    class Meta:
        model = models.AjusteStockDetalle
        fields = ['item', 'cantidad',]
        #widgets = {'cantidad':DecimalMaskInput}
