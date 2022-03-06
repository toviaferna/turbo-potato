from django_filters import FilterSet
from .models import Deposito, Item

class DepositoFilter(FilterSet):
    class Meta:
        model = Deposito
        fields = ["es_planta_acopiadora",]

class ItemFilter(FilterSet):
    class Meta:
        model = Item
        fields = ["categoria","marca","tipo_item","tipo_impuesto","es_activo"]