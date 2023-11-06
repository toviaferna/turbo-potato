
from apps.finance import models
from core.layouts import CancelButton, FormActions, SaveButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Layout, Row
from django.forms.models import ModelForm


class PersonaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("documento"),
                Column("razon_social"),
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
            FormActions()
        )

    class Meta:
        model = models.Persona
        fields = ["razon_social","documento","celular","pais","localidad","direccion","es_cliente","es_proveedor","es_empleado"]

class BancoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            FormActions()
        )
    class Meta:
        model = models.Banco
        fields = ["descripcion",]

class CuentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("descripcion", ),
                Column("es_banco", css_class="col-sm-2"),
            ),
            Row(
                Column("nro_cuenta"),
                Column("banco")
            ),
            FormActions()
            
        )
    class Meta:
        model = models.Cuenta
        fields = ["descripcion","es_banco","nro_cuenta","banco"]

class PaisForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "abreviatura",
            FormActions()
        )
    class Meta:
        model = models.Pais
        fields = ["descripcion", "abreviatura"]

class DepartamentoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            FormActions()
        )
    class Meta:
        model = models.Departamento
        fields = ["descripcion",]

class DistritoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "departamento",
            FormActions()
        )
    class Meta:
        model = models.Distrito
        fields = ["descripcion","departamento",]

class LocalidadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "distrito",
            FormActions()
        )
    class Meta:
        model = models.Localidad
        fields = ["descripcion","distrito"]

class TipoImpuestoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "porcentaje",
            "es_iva",
            FormActions()
        )
    class Meta:
        model = models.TipoImpuesto
        fields = ["descripcion","porcentaje","es_iva"]
