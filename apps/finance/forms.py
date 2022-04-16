
from django.forms.models import ModelForm
from core.layouts import CancelButton, SaveButton
from .models import Banco, Cuenta, Departamento, Distrito, Localidad, Pais, Persona, TipoImpuesto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder,Layout, Submit, Row, Column

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
        model = Persona
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
        model = Banco
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
        model = Cuenta
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
        model = Pais
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
        model = Departamento
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
        model = Distrito
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
        model = Localidad
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
        model = TipoImpuesto
        fields = ['descripcion','porcentaje','es_iva']