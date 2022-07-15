
from apps.finance import models
from core.layouts import CancelButton, SaveButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Layout, Row
from django.forms.models import ModelForm


class PersonaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("razon_social"),
                Column("documento"),
            ),
            Row(
                Column("celular"),
                Column("pais"),
            ),
            Row(
                Column("localidad"),
                Column("direccion"),
            ),
            Row(
                Column("es_cliente"),
                Column("es_proveedor"),
                Column("es_empleado"),
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.Persona
        fields = ['razon_social',"documento","celular","pais","localidad","direccion","es_cliente","es_proveedor","es_empleado"]

class BancoForm(ModelForm):
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
        model = models.Banco
        fields = ['descripcion',]

class CuentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("descripcion", css_class="col-md my-1"),
                Column("es_banco", css_class="col-md my-1 mt-4"),
                css_class="align-items-center"
            ),
            Row(
                Column("nro_cuenta"),
                Column("banco")
            ),
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
            
        )
    class Meta:
        model = models.Cuenta
        fields = ['descripcion',"es_banco","nro_cuenta","banco"]

class PaisForm(ModelForm):
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
        model = models.Pais
        fields = ['descripcion',]

class DepartamentoForm(ModelForm):
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
        model = models.Departamento
        fields = ['descripcion',]

class DistritoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "departamento",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.Distrito
        fields = ['descripcion','departamento',]

class LocalidadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "distrito",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.Localidad
        fields = ['descripcion','distrito']

class TipoImpuestoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "porcentaje",
            "es_iva",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = models.TipoImpuesto
        fields = ['descripcion','porcentaje','es_iva']
