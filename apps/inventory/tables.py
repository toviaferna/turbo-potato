from .models import Categoria, Deposito, Item, Marca, TipoItem
from core.tables import AccionTable

class MarcaTable(AccionTable):
    class Meta:
        model = Marca
        fields = ("descripcion",)

class CategoriaTable(AccionTable):
    class Meta:
        model = Categoria
        fields = ("descripcion",)

class DepositoTable(AccionTable):
    class Meta:
        model = Deposito
        fields = ("descripcion","es_planta_acopiadora")

class TipoItemTable(AccionTable):
    class Meta:
        model = TipoItem
        fields = ("descripcion",)

class ItemTable(AccionTable):
    class Meta:
        model = Item
        fields = ("descripcion","categoria","marca","tipo_impuesto","costo","ultimo_costo","precio","es_activo")