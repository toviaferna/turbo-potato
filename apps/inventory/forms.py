from django.forms.models import ModelForm
from core.layouts import CancelButton, Formset
from .models import AjusteStock, AjusteStockDetalle, Categoria, Deposito, Item, Marca, TipoItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder,Layout, Submit, Row, Column, Fieldset
from core.widgets import DateInput
from apps.finance.models import Persona

class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = Marca
        fields = ['descripcion',]

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = Categoria
        fields = ['descripcion',]

class TipoItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = TipoItem
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
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = Item
        fields = ['descripcion','codigo_barra','tipo_item','categoria','marca','tipo_impuesto','precio','es_activo']

class DepositoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "es_planta_acopiadora",
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = Deposito
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
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
       model = AjusteStock
       fields = ['fecha_documento','comprobante','empleado','deposito','observacion',]
       widgets = { 'fecha_documento':DateInput }

class AjusteStockDetalleForm(ModelForm):
    class Meta:
        model = AjusteStockDetalle
        fields = ['item', 'cantidad',]
        #widgets = {'cantidad':DecimalMaskInput}