from .models import Finca
from core.tables import AccionTable

class FincaTable(AccionTable):
    class Meta:
        model = Finca
        fields = ("descripcion","dimensionHa","ubicacion")

