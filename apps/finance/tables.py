from .models import Banco, Cuenta, Departamento, Distrito, Localidad, Pais, Persona, TipoImpuesto
from core.tables import EditableTable

class PersonaTable(EditableTable):
    class Meta:
        model = Persona
        fields = ("razon_social","documento","celular")

class BancoTable(EditableTable):
    class Meta:
        model = Banco
        fields = ("descripcion",)

class CuentaTable(EditableTable):
    class Meta:
        model = Cuenta
        fields = ("descripcion","banco","nro_cuenta")

class PaisTable(EditableTable):
    class Meta:
        model = Pais
        fields = ("descripcion",)

class DepartamentoTable(EditableTable):
    class Meta:
        model = Departamento
        fields = ("descripcion",)

class DistritoTable(EditableTable):
    class Meta:
        model = Distrito
        fields = ("descripcion","departamento")

class LocalidadTable(EditableTable):
    class Meta:
        model = Localidad
        fields = ("descripcion","distrito")

class TipoImpuestoTable(EditableTable):
    class Meta:
        model = TipoImpuesto
        fields = ("descripcion","porcentaje","es_iva")