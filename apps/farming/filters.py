import django_filters
from django_filters import FilterSet

from apps.farming import models
from core.widgets import DateInput


class ActividadAgricolaFilter(FilterSet):
    fecha_documento = django_filters.DateFilter(
        widget=DateInput(),
        field_name="fecha_documento",
        label="Doc.",
    )
    class Meta:
        model = models.ActividadAgricola
        fields = [
            "fecha_documento", 
            "tipo_actividad_agricola", 
            "lote", 
            "zafra", 
            "finca",
            "es_servicio_contratado",
            "es_vigente"
        ]

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
