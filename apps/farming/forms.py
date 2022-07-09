from apps.finance.models import Persona
from apps.inventory.models import Deposito, Item
from core.layouts import CancelButton, Formset, NextButton, SaveButton
from core.widgets import (DateInput, FormulaInput, ItemCustomSelect,
                          MaquinariaCustomSelect, SumInput)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, ButtonHolder, Column, Fieldset, Layout,
                                 Row)
from django.forms import BooleanField, CharField, DateField, DecimalField
from django.forms.models import ModelForm

from .models import (Acopio, AcopioCalificacion, AcopioDetalle,
                     ActividadAgricola, ActividadAgricolaItemDetalle,
                     ActividadAgricolaMaquinariaDetalle, CalificacionAgricola,
                     CierreZafra, CierreZafraDetalle, Contrato, Finca,
                     LiquidacionAgricola, LiquidacionAgricolaDetalle, Lote,
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
        widgets = {'fecha_documento':DateInput,} #'cantidadTrabajada': DecimalMaskInput}

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
                u'Detalles',
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

class LiquidacionAgricolaSelectionForm(ModelForm):
    class Meta:
        model = LiquidacionAgricola
        fields = ['tipo','zafra','proveedor','precio_unitario']
        #widgets = {'precioUnitario':DecimalMaskInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["proveedor"].queryset = Persona.objects.filter(es_proveedor=True)
        self.helper.layout = Layout(
            Row(
                Column("tipo",),
                Column("zafra",),
            ),
            Row(
                Column("proveedor",),
                Column("precio_unitario",),
            ),
            ButtonHolder(
                NextButton(),
                CancelButton(),
            ),
        )

class LiquidacionAgricolaForm(ModelForm):
    total = DecimalField(
        widget=SumInput('subtotal'),
    )
    class Meta:
        model = LiquidacionAgricola
        fields = ['fecha_documento','tipo','zafra','proveedor','precio_unitario','observacion']
        widgets = {'fecha_documento':DateInput,}#'precioUnitario':DecimalMaskInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['total'].label = False
        #self.fields['total'].widget = DecimalMaskInput()
        self.fields["proveedor"].queryset = Persona.objects.filter(es_proveedor=True)
        self.helper.layout = Layout(
            Row(
                Column("fecha_documento", css_class="col-sm-3"),
                Column("tipo", css_class="col-sm-5"),
                Column("zafra",),
            ),
            Row(
                Column("proveedor",),
                Column("precio_unitario", css_class="col-sm-2"),
                Column("observacion",),
            ),
            Fieldset(
                u'Detalles',
                Formset(
                    "LiquidacionAgricolaDetalleInline"#, stacked=True
                )
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

class LiquidacionAgricolaDetalleForm(ModelForm):
    
    check = BooleanField(label='Sel.',required=False)
    movimiento = CharField(max_length=300,disabled = True)
    sub_total = DecimalField(max_digits=15,disabled = True)
    #sub_total.label = "Sub Total"
    
    class Meta:
        model = LiquidacionAgricolaDetalle
        fields = ['secuencia_origen','finca','lote','cantidad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        
class CierreZafraSelectionForm(ModelForm):
    class Meta:
        model = CierreZafra
        fields = ['zafra']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["zafra"].queryset =  Zafra.objects.filter(esta_cerrado=False)
        self.helper.layout = Layout(
            "zafra",
            ButtonHolder(
                NextButton(),
                CancelButton(),
            ),
        )

class CierreZafraForm(ModelForm):

    total_costo_v = DecimalField(
        widget=SumInput('costo_total'),
    )
    total_acopiado_v = DecimalField(
        widget=SumInput('cantidad_acopio_neto'),
    )
    total_cultivado_v = DecimalField(
        widget=SumInput('ha_cultivada'),
    )
    class Meta:
        model = CierreZafra
        fields = ['fecha', 'zafra', 'observacion']
        widgets = {'fecha':DateInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['total_costo_v'].label = False
        self.fields['total_acopiado_v'].label = False
        self.fields['total_cultivado_v'].label = False
        
        self.helper.layout = Layout(
            Row(
                Column("fecha", css_class="col-sm-3"),
                Column("zafra",),
            ),
            "observacion",
            Fieldset(
                u'Detalles',
                Formset(
                    "CierreZafraDetalleInline"#, stacked=True
                ),  
            ), 
            Row(
                Column(
                    HTML('<label> Total HA Cultivada: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total_cultivado_v", css_class="col-sm-2")
            ),
            Row(
                Column(
                    HTML('<label> Total Acopiado: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total_acopiado_v", css_class="col-sm-2")
            ),
            Row(
                Column(
                    HTML('<label> Total Costo: </label>'),
                    css_class='text-right col-sm-9 mt-2'
                ),
                Column("total_costo_v", css_class="col-sm-2")
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton()
            )
        )

class CierreZafraDetalleForm(ModelForm):
    check = BooleanField(label='Sel.',required=False)
    class Meta:
        model = CierreZafraDetalle
        fields = ['check','finca','ha_cultivada','cantidad_acopio_neto','rendimiento','costo_total','costo_ha','costo_unitario']
        #widgets = {'ha_cultivada':DecimalMaskInput,'cantidad_acopio_neto':DecimalMaskInput,'cantidad_acopio_neto':DecimalMaskInput,'rendimiento':DecimalMaskInput,'costo_total':DecimalMaskInput,'costoHA':DecimalMaskInput,'costoUnit':DecimalMaskInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['finca'].widget.attrs.update({'readonly':True, 'style': 'pointer-events:none;'})
        self.fields['ha_cultivada'].widget.attrs.update({'readonly':True, 'style': 'pointer-events:none;'})
        self.fields['cantidad_acopio_neto'].widget.attrs.update({'readonly':True, 'style': 'pointer-events:none;'})
        self.fields['rendimiento'].widget.attrs.update({'readonly':True, 'style': 'pointer-events:none;'})
        self.fields['costo_total'].widget.attrs.update({'readonly':True, 'style': 'pointer-events:none;'})
        self.fields['costo_ha'].widget.attrs.update({'readonly':True, 'style': 'pointer-events:none;'})
        self.fields['costo_unitario'].widget.attrs.update({'readonly':True, 'style': 'pointer-events:none;'})
