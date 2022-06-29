from apps.inventory.models import Item
from core.layouts import CancelButton, Formset, SaveButton
from core.widgets import DateInput, SumInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, ButtonHolder, Column, Fieldset, Layout,
                                 Row)
from django.forms import DateField, DecimalField
from django.forms.models import ModelForm

from .models import (CalificacionAgricola, Contrato, Finca, Lote,
                     MaquinariaAgricola, PlanActividadZafra,
                     PlanActividadZafraDetalle, TipoActividadAgricola,
                     TipoMaquinariaAgricola, Zafra)


class FincaForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "dimension_ha",
            "ubicacion",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),               
        )
    class Meta:
        model = Finca
        fields = ['descripcion','dimension_ha','ubicacion']

class CalificacionAgricolaForm(ModelForm):
    
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
        model = CalificacionAgricola
        fields = ['descripcion',]

class TipoMaquinariaAgricolaForm(ModelForm):
    
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
        model = TipoMaquinariaAgricola
        fields = ['descripcion',]

class MaquinariaAgricolaForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("descripcion"),
                Column("tipo_maquinaria_agricola")
            ), 
            Row(
                Column("precio",css_class="col-sm-6"),
            ),
            "es_implemento",
            "admite_implemento",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = MaquinariaAgricola
        fields = ["descripcion","tipo_maquinaria_agricola", "es_implemento","admite_implemento","precio"]

class TipoActividadAgricolaForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("descripcion"),
            ),
            Row(
                Column("es_cosecha", ),
                Column("es_siembra", ),
                Column("es_resiembra", ),
                css_class="col-sm-6"
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = TipoActividadAgricola
        fields = ['descripcion','es_cosecha','es_siembra','es_resiembra']

class ZafraForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["item"].queryset = Item.objects.filter(tipo_item__pk=1)
        self.helper.layout = Layout(
            Row(
                Column("descripcion"),
                Column("item", ),
            ),
            Row(
                Column("anho", ),
                Column("kg_estimado", ),
            ),
            'es_zafrinha',
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = Zafra
        fields = ['descripcion','item','anho','es_zafrinha','kg_estimado']

class LoteForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("descripcion"),
                Column("zafra", ),
            ),
            Row(
                Column("finca", ),
                Column("dimension", ),
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = Lote
        fields = ['descripcion','zafra','finca','dimension']

class PlanActividadZafraForm(ModelForm):
    total = DecimalField(
        widget=SumInput('costo'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['total'].label = False
        self.helper.layout = Layout(
            Row(
                Column("fecha", css_class="col-sm-3"),
                Column("zafra",)
            ),
            "observacion",
            Fieldset(
                u'Detalles',
                Formset("PlanActividadZafraDetalleInline"), 
            ),
            Row(
                Column(
                    HTML('<label> Total: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total", css_class="col-sm-2")
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton()
            )
        )

    class Meta:
        model = PlanActividadZafra
        fields = ['fecha', 'zafra', 'observacion']
        widgets = {'fecha':DateInput}

class PlanActividadZafraDetalleForm(ModelForm):
    fecha_actividad = DateField(widget=DateInput, label="Fecha Act.")
    class Meta:
        model = PlanActividadZafraDetalle
        fields = ['fecha_actividad', 'finca', 'tipo_actividad_agricola', 'descripcion','costo']
        widgets = { 
            'fechaActividad':DateInput,
            #'costo': DecimalMaskInput 
        }

class ContratoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        #self.fields['costoPactado'].widget = DecimalMaskInput()
        self.helper.layout = Layout(
            Row(
                Column("fecha", css_class="col-sm-3"),
                Column("zafra"),
                Column("persona"),
            ),
            Row(
                Column("descripcion"),
                Column("costo_pactado", css_class="col-sm-3"),
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton()
            )
        )

    class Meta:
        model = Contrato
        fields = ['fecha','zafra','persona','descripcion','costo_pactado']
        widgets = {'fecha':DateInput}
