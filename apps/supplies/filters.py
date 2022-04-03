from django.forms import CheckboxInput
from django_filters import FilterSet, DateFilter
from django_filters.filters import DateFilter
from apps.supplies.models import Compra
import django_filters
from core.widgets import DateInput

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
        field_name='fecha_documento', 
        lookup_expr='gte', 
        label='Desde'
    )
    fecha_hasta = django_filters.DateFilter(
        widget=DateInput(), 
        field_name='fecha_documento', 
        lookup_expr='lte', 
        label='Hasta'
    )

    def __init__(self, *args, **kwargs):
        super(CompraFilter, self).__init__(*args, **kwargs)
        self.form.initial['es_vigente'] = True

    class Meta:
        model = Compra
        fields = ["fecha_desde","fecha_hasta","es_vigente", "es_credito"]
    