from django_filters import FilterSet
from .models import Cuenta, Distrito, Localidad, Persona

class DistritoFilter(FilterSet):
    class Meta:
        model = Distrito
        fields = ["departamento",]

class LocalidadFilter(FilterSet):
    class Meta:
        model = Localidad
        fields = ["distrito",]

class CuentaFilter(FilterSet):
    class Meta:
        model = Cuenta
        fields = ["es_banco",]

class PersonaFilter(FilterSet):
    class Meta:
        model = Persona
        fields = ["es_cliente","es_proveedor","es_empleado","pais","localidad"]