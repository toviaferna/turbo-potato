from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Field, Layout, Row
from django_filters import FilterSet, ModelChoiceFilter

from apps.finance import models
from core.widgets import AutocompleteSelect


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
    # localidad = ModelChoiceFilter(
    #     queryset=models.Localidad.objects.all(),
    #     widget= AutocompleteSelect(
    #         url="localidad_autocomplete",
    #     )
    # )
    class Meta:
        model = models.Persona
        fields = ["es_cliente","es_proveedor","es_empleado","pais"]