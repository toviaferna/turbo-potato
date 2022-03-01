from .models import Finca
from core.tables import EditableTable

class FincaTable(EditableTable):
    class Meta:
        model = Finca
        fields = ("descripcion","dimensionHa","ubicacion")

