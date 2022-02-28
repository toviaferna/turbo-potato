from core.tables import BaseTable
from .models import Finca

class FincaTable(BaseTable):
    class Meta:
        model = Finca
        fields = ("descripcion","dimensionHa","ubicacion")