from .models import Banco, Cuenta, Departamento, Distrito, Localidad, Pais, Persona, TipoImpuesto
from core.tables import AccionTable

class PersonaTable(AccionTable):
    class Meta:
        model = Persona
        fields = ("razon_social","documento","celular")

class BancoTable(AccionTable):
    class Meta:
        model = Banco
        fields = ("descripcion",)

class CuentaTable(AccionTable):
    class Meta:
        model = Cuenta
        fields = ("descripcion","banco","nro_cuenta")

class PaisTable(AccionTable):
    class Meta:
        model = Pais
        fields = ("descripcion",)

class DepartamentoTable(AccionTable):
    class Meta:
        model = Departamento
        fields = ("descripcion",)

class DistritoTable(AccionTable):
    class Meta:
        model = Distrito
        fields = ("descripcion","departamento")

class LocalidadTable(AccionTable):
    class Meta:
        model = Localidad
        fields = ("descripcion","distrito")

class TipoImpuestoTable(AccionTable):
    class Meta:
        model = TipoImpuesto
        fields = ("descripcion","porcentaje","es_iva")