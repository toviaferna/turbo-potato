import django_filters
from apps.supplies.models import Compra
from core.widgets import DateInput
from django_filters import FilterSet

# class PedidoCompraFilter(FilterSet):
#     fecha_desde = DateFilter(
#         widget=DateInput(
#             attrs={
#                 'placeholder': '1970-01-01'
#             }
#         ),
#         field_name='fecha_documento',
#         lookup_expr='gte',
#         label='Desde'
#     )


class CompraFilter(FilterSet):
    fecha_desde = django_filters.DateFilter(
        widget=DateInput(),
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
        super(CompraFilter, self).__init__(*args, **kwargs)
        self.form.initial["es_vigente"] = True

    class Meta:
        model = Compra
        fields = ["fecha_desde", "fecha_hasta", "es_vigente", "es_credito"]


class LibroCompraFilter(FilterSet):
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

    def __init__(self, *args, **kwargs):
        super(LibroCompraFilter, self).__init__(*args, **kwargs)
        self.form.initial["es_vigente"] = True

    class Meta:
        model = Compra
        fields = [
            "fecha_desde",
            "fecha_hasta",
            "comprobante",
            "proveedor",
            "deposito",
            "es_credito",
            "es_vigente",
        ]
