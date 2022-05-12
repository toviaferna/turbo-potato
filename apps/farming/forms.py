from core.layouts import CancelButton, SaveButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Layout, Row, Submit
from django.forms.models import ModelForm

from .models import (CalificacionAgricola, Finca, Lote, MaquinariaAgricola,
                     TipoActividadAgricola, TipoMaquinariaAgricola, Zafra)
from apps.inventory.models import Item

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
