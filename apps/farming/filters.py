from apps.farming import models
from django_filters import FilterSet


class TipoActividadAgricolaFilter(FilterSet):
    class Meta:
        model = models.TipoActividadAgricola
        fields = ["es_cosecha", "es_siembra", "es_resiembra"]


class ZafraFilter(FilterSet):
    class Meta:
        model = models.Zafra
        fields = [
            "esta_cerrado",
        ]


class PlanActividadZafraFilter(FilterSet):
    # falta agregar filtros de fecha
    class Meta:
        model = models.PlanActividadZafra
        fields = ["fecha", "zafra"]
