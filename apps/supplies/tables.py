from .models import Marca
from core.tables import EditableTable

class MarcaTable(EditableTable):
    class Meta:
        model = Marca
        fields = ("descripcion",)