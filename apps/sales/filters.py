from django_filters import FilterSet
from apps.sales.models import AperturaCaja

class AperturaCajaFilter(FilterSet):
    class Meta:
        model = AperturaCaja
        fields = ["empleado", "esta_cerrado",]