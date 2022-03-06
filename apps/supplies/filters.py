from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from django_filters.filters import DateFilter

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
    