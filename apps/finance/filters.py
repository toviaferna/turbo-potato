from apps.finance import models
from django_filters import FilterSet


class DistritoFilter(FilterSet):
    class Meta:
        model = models.Distrito
        fields = ["departamento",]

class LocalidadFilter(FilterSet):
    class Meta:
        model = models.Localidad
        fields = ["distrito",]

class CuentaFilter(FilterSet):
    class Meta:
        model = models.Cuenta
        fields = ["es_banco",]

class PersonaFilter(FilterSet):
    class Meta:
        model = models.Persona
        fields = ["es_cliente","es_proveedor","es_empleado","pais","localidad"]
