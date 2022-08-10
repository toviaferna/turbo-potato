import django_filters
from apps.farming.models import ActividadAgricola
from apps.finance.models import Persona
from apps.inventory.models import ItemMovimiento
from apps.sales.models import Venta
from apps.supplies.models import Compra
from core.widgets import DateInput
from django_filters import FilterSet


class CompraInformeFilter(FilterSet):
    fecha_desde = django_filters.DateFilter(
        widget=DateInput(attrs={"placeholder": "1970-01-01"}),
        field_name="fecha_documento",
        lookup_expr="gte",
        label="Desde",
    )
    fecha_hasta = django_filters.DateFilter(
        widget=DateInput(),
        field_name="fecha_documento",
        lookup_expr="lte",
        label="Hasta",
    )
    fecha_documento = django_filters.DateRangeFilter(label="Rango")

    def __init__(self, *args, **kwargs):
        super(CompraInformeFilter, self).__init__(*args, **kwargs)
        self.form.initial["es_vigente"] = True
        self.form.fields["proveedor"].queryset = Persona.objects.filter(
            es_proveedor=True
        )

    class Meta:
        model = Compra
        fields = [
            "fecha_documento",
            "fecha_desde",
            "fecha_hasta",
            "comprobante",
            "proveedor",
            "deposito",
            "cuenta",
            "es_credito",
            "es_vigente",
        ]


class VentaInformeFilter(FilterSet):
    fecha_desde = django_filters.DateFilter(
        widget=DateInput(attrs={"placeholder": "1970-01-01"}),
        field_name="fecha_documento",
        lookup_expr="gte",
        label="Desde",
    )
    fecha_hasta = django_filters.DateFilter(
        widget=DateInput(),
        field_name="fecha_documento",
        lookup_expr="lte",
        label="Hasta",
    )
    fecha_documento = django_filters.DateRangeFilter(label="Rango")

    def __init__(self, *args, **kwargs):
        super(VentaInformeFilter, self).__init__(*args, **kwargs)
        self.form.initial["es_vigente"] = True
        self.form.fields["cliente"].queryset = Persona.objects.filter(es_cliente=True)

    class Meta:
        model = Venta
        fields = [
            "fecha_documento",
            "fecha_desde",
            "fecha_hasta",
            "comprobante",
            "cliente",
            "deposito",
            "cuenta",
            "es_credito",
            "es_vigente",
        ]


class ProduccionAgricolaInformeFilter(FilterSet):
    fecha_desde = django_filters.DateFilter(
        widget=DateInput(attrs={"placeholder": "1970-01-01"}),
        field_name="fecha_documento",
        lookup_expr="gte",
        label="Desde",
    )
    fecha_hasta = django_filters.DateFilter(
        widget=DateInput(),
        field_name="fecha_documento",
        lookup_expr="lte",
        label="Hasta",
    )
    fecha_documento = django_filters.DateRangeFilter(label="Rango")

    def __init__(self, *args, **kwargs):
        super(ProduccionAgricolaInformeFilter, self).__init__(*args, **kwargs)
        self.form.initial["es_vigente"] = True
        self.form.fields["empleado"].queryset = Persona.objects.filter(es_empleado=True)

    class Meta:
        model = ActividadAgricola
        fields = [
            "fecha_documento",
            "fecha_desde",
            "fecha_hasta",
            "tipo_actividad_agricola",
            "zafra",
            "finca",
            "lote",
            "empleado",
            "es_servicio_contratado",
            "es_vigente",
        ]


class InventarioDepositoInformeFilter(FilterSet):
    fecha_desde = django_filters.DateFilter(
        widget=DateInput(attrs={"placeholder": "1970-01-01"}),
        field_name="fecha_documento",
        lookup_expr="gte",
        label="Desde",
    )
    fecha_hasta = django_filters.DateFilter(
        widget=DateInput(),
        field_name="fecha_documento",
        lookup_expr="lte",
        label="Hasta",
    )

    def __init__(self, *args, **kwargs):
        super(InventarioDepositoInformeFilter, self).__init__(*args, **kwargs)
        self.form.initial["es_vigente"] = True

    class Meta:
        model = ItemMovimiento
        fields = [
            "fecha_desde",
            "fecha_hasta",
            "tipo_movimiento",
            "item",
            "deposito",
            "es_vigente",
        ]
