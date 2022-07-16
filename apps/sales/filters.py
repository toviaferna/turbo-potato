from apps.sales import models
from django_filters import FilterSet


class AperturaCajaFilter(FilterSet):
    class Meta:
        model = models.AperturaCaja
        fields = ["empleado", "esta_cerrado",]
