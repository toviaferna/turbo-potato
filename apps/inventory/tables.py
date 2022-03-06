from .models import Categoria, Deposito, Item, Marca, TipoItem
from core.tables import EditableTable

class MarcaTable(EditableTable):
    class Meta:
        model = Marca
        fields = ("descripcion",)

class CategoriaTable(EditableTable):
    class Meta:
        model = Categoria
        fields = ("descripcion",)

class DepositoTable(EditableTable):
    class Meta:
        model = Deposito
        fields = ("descripcion","es_planta_acopiadora")

class TipoItemTable(EditableTable):
    class Meta:
        model = TipoItem
        fields = ("descripcion",)

class ItemTable(EditableTable):
    class Meta:
        model = Item
        fields = ("descripcion","categoria","marca","tipo_impuesto","costo","ultimo_costo","precio","es_activo")