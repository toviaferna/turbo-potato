from apps.inventory import models
from django_filters import FilterSet


class DepositoFilter(FilterSet):
    class Meta:
        model = models.Deposito
        fields = ["es_planta_acopiadora",]

class ItemFilter(FilterSet):
    class Meta:
        model = models.Item
        fields = ["categoria","marca","tipo_item","tipo_impuesto","es_activo"]
