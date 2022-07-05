from apps.finance.models import Persona
from apps.inventory.models import Deposito, Item
from core.layouts import CancelButton, Formset, SaveButton
from core.widgets import (DateInput, FormulaInput, ItemCustomSelect,
                          MaquinariaCustomSelect, SumInput)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, ButtonHolder, Column, Fieldset, Layout,
                                 Row)
from django.forms import DateField, DecimalField
from django.forms.models import ModelForm

from .models import (Acopio, AcopioCalificacion, AcopioDetalle,
                     ActividadAgricola, ActividadAgricolaItemDetalle,
                     ActividadAgricolaMaquinariaDetalle, CalificacionAgricola,
                     Contrato, Finca, Lote, MaquinariaAgricola,
                     PlanActividadZafra, PlanActividadZafraDetalle,
                     TipoActividadAgricola, TipoMaquinariaAgricola, Zafra)


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

class AcopioForm(ModelForm):
    class Meta:
        model = Acopio
        fields = ['fecha', 'zafra', 'deposito', 'conductor','conductor','camion','comprobante','peso_bruto','peso_tara','peso_descuento','peso_bonificacion','es_transportadora_propia','observacion']
        #widgets = {'fecha':DateInput,'pBruto':DecimalMaskInput,'pTara':DecimalMaskInput,'pDescuento':DecimalMaskInput,'pBonificacion':DecimalMaskInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields["deposito"].queryset =  Deposito.objects.filter(es_planta_acopiadora=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha",css_class="col-sm-3"),
                Column("zafra",),
                Column("deposito",),
            ),
            Row(
                Column("conductor",),
                Column("camion",),
                Column("comprobante",css_class="col-sm-3"),
            ),
            Row(
                Column("peso_bruto",),
                Column("peso_tara",),
                Column("peso_descuento",),
                Column("peso_bonificacion",),
            ),
            "observacion",
            "es_transportadora_propia",
            Fieldset(
                u'Detalles',
                Formset(
                    "AcopioDetalleInline",#, stacked=True
                ), 
                Formset(
                    "AcopioCalificacionDetalleInline",#, stacked=True
                ), 
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton()
            )
        )

class AcopioDetalleForm(ModelForm):
    class Meta:
        model = AcopioDetalle
        fields = ['acopio', 'finca', 'lote', 'peso']
        #widgets = {'peso':DecimalMaskInput}

class AcopioCalificacionForm(ModelForm):
    class Meta:
        model = AcopioCalificacion
        fields = ['acopio', 'calificacion_agricola', 'grado', 'porcentaje', 'peso']
        #widgets = {'grado':DecimalMaskInput,'porcentaje':DecimalMaskInput,'peso':DecimalMaskInput}

class ActividadAgricolaForm(ModelForm):
    total_maquinaria = DecimalField(
        widget=SumInput('subtotal_maquinaria'),
    )
    total_item = DecimalField(
        widget=SumInput('subtotalItem'),
    )
    class Meta:
        model = ActividadAgricola
        fields = ['fecha_documento','tipo_actividad_agricola','zafra', 'finca','lote','es_servicio_contratado','empleado','cantidad_trabajada','observacion']
        #widgets = {'fechaDocumento':DateInput,'cantidadTrabajada': DecimalMaskInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['total_maquinaria'].label = False
        #self.fields['totalMaquinaria'].widget = DecimalMaskInput()
        self.fields['total_item'].label = False
        #self.fields['totalItem'].widget = DecimalMaskInput()
        self.fields["empleado"].queryset = Persona.objects.filter(es_empleado=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-3"),
                Column("tipo_actividad_agricola",),
                Column( "zafra",),
            ),
            Row(
                Column("finca",),
                Column("lote",),
                Column("cantidad_trabajada",css_class="col-sm-2"),
            ),
            Row(
                Column("empleado",css_class="col-sm-4"),
                Column("observacion",),
            ),
            "es_servicio_contratado",
            Fieldset(
                u'Detalle',
                Formset(
                    "ActividadAgricolaMaquinariaDetalleInline"#, stacked=True
                ), 
                Formset(
                    "ActividadAgricolaItemDetalleInline",#, stacked=True
                ),       
            ),
            Row(
                Column(
                    HTML('<label> Total Máquina: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total_maquinaria", css_class="col-sm-2")
            ),
            Row(
                Column(
                    HTML('<label> Total Items: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total_item", css_class="col-sm-2")
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton()
            )
        )

class ActividadAgricolaMaquinariaDetalleForm(ModelForm):
    subtotal_maquinaria = DecimalField(
        widget=FormulaInput('precio*ha_trabajada'),
        label = "SubTotal"
    )

    class Meta:
        model = ActividadAgricolaMaquinariaDetalle
        fields = ['maquinaria', 'ha_trabajada','precio','subtotal_maquinaria']
        #widgets = {'haTrabajada':DecimalMaskInput,'precio':DecimalMaskInput,'subtotalMaquinaria':DecimalMaskInput}

class ActividadAgricolaItemDetalleForm(ModelForm):
    subtotal_item = DecimalField(
        widget=FormulaInput('costo*cantidad'),
        label = "SubTotal"
    )
    class Meta:
        model = ActividadAgricolaItemDetalle
        fields = ['item', 'deposito','dosis','costo','cantidad','porcentaje_impuesto','subtotal_item']
        #widgets = {'dosis':DecimalMaskInput,'costo':DecimalMaskInput,'cantidad':DecimalMaskInput,'porcentajeImpuesto':DecimalMaskInput,'subtotalItem':DecimalMaskInput}
