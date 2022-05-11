from django_filters import FilterSet
from apps.farming.models import TipoActividadAgricola

class TipoActividadAgricolaFilter(FilterSet):
    class Meta:
        model = TipoActividadAgricola
        fields = ["es_cosecha","es_siembra","es_resiembra"]