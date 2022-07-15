from apps.finance import models
from core.tables import AccionTable


class PersonaTable(AccionTable):
    class Meta:
        model = models.Persona
        fields = ("razon_social","documento","celular")

class BancoTable(AccionTable):
    class Meta:
        model = models.Banco
        fields = ("descripcion",)

class CuentaTable(AccionTable):
    class Meta:
        model = models.Cuenta
        fields = ("descripcion","banco","nro_cuenta")

class PaisTable(AccionTable):
    class Meta:
        model = models.Pais
        fields = ("descripcion",)

class DepartamentoTable(AccionTable):
    class Meta:
        model = models.Departamento
        fields = ("descripcion",)

class DistritoTable(AccionTable):
    class Meta:
        model = models.Distrito
        fields = ("descripcion","departamento")

class LocalidadTable(AccionTable):
    class Meta:
        model = models.Localidad
        fields = ("descripcion","distrito")

class TipoImpuestoTable(AccionTable):
    class Meta:
        model = models.TipoImpuesto
        fields = ("descripcion","porcentaje","es_iva")
