import django_filters
from django_filters import FilterSet

from apps.sales import models
from core.widgets import DateInput


class AperturaCajaFilter(FilterSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["empleado"].queryset = models.Persona.objects.filter(es_empleado=True)
    class Meta:
        model = models.AperturaCaja
        fields = [
            "empleado",
            "esta_cerrado",
        ]


class LibroVentaFilter(FilterSet):
    fecha_desde = django_filters.DateFilter(
        widget=DateInput(attrs={"placeholder": "1970-01-01"}),
        field_name="fechaDocumento",
        lookup_expr="gte",
        label="Desde",
    )
    fecha_hasta = django_filters.DateFilter(
        widget=DateInput(),
        field_name="fechaDocumento",
        lookup_expr="lte",
        label="Hasta",
    )
    # fechaDocumento = django_filters.DateRangeFilter(label='Rango')

    def __init__(self, *args, **kwargs):
        super(LibroVentaFilter, self).__init__(*args, **kwargs)
        self.form.initial["es_vigente"] = True

    class Meta:
        model = models.Venta
        fields = [
            "fecha_desde",
            "fecha_hasta",
            "comprobante",
            "cliente",
            "deposito",
            "es_credito",
            "es_vigente",
        ]
