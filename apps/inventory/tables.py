from core.tables import AccionTable
from core.tables.columns import NumericColumn

from .models import AjusteStock, Categoria, Deposito, Item, Marca, TipoItem


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
    costo = NumericColumn()
    ultimo_costo = NumericColumn()
    precio = NumericColumn()
    class Meta:
        model = Item
        fields = ("descripcion","categoria","marca","tipo_impuesto","costo","ultimo_costo","precio","es_activo")

class AjusteStockTable(AccionTable):
    class Meta:
        model = AjusteStock
        fields = ("fecha_documento","comprobante","empleado","deposito","observacion",)
