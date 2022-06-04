from django_filters import FilterSet
from apps.farming.models import PlanActividadZafra, TipoActividadAgricola, Zafra

class TipoActividadAgricolaFilter(FilterSet):
    class Meta:
        model = TipoActividadAgricola
        fields = ["es_cosecha","es_siembra","es_resiembra"]

class ZafraFilter(FilterSet):
    class Meta:
        model = Zafra
        fields = ["esta_cerrado",]

class PlanActividadZafraFilter(FilterSet):
    #falta agregar filtros de fecha
    class Meta:
        model = PlanActividadZafra
        fields = ["fecha","zafra"]