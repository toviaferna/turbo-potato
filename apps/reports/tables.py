from apps.farming.models import ActividadAgricola
from apps.inventory.models import ItemMovimiento
from apps.sales.models import Venta
from apps.supplies.models import Compra
from core.tables import DetailTable, columns


class CompraInformeTable(DetailTable):
    total = columns.NumericColumn(verbose_name='Total',)
    class Meta:
        model = Compra
        fields = ("fecha_documento","es_credito","comprobante","proveedor","total",)

class VentaInformeTable(DetailTable):
    total = columns.NumericColumn(verbose_name= 'Total',)
    class Meta:
        model = Venta
        fields = ("fecha_documento","es_credito","comprobante","cliente","total",)

class ProduccionAgricolaInformeTable(DetailTable):   
    total_maquinaria = columns.NumericColumn(verbose_name= 'Total Maqui.',)
    total_item = columns.NumericColumn(verbose_name= 'Total Item',)
    total = columns.NumericColumn(verbose_name= 'Total',)
    class Meta:
        model = ActividadAgricola
        fields = ("fecha_documento","tipo_actividad_agricola","zafra","finca","lote","total_maquinaria","total_item","total")

class InventarioDepositoInformeTable(DetailTable):   
    cantidad = columns.NumericColumn(verbose_name='Cantidad')
    class Meta:
        model = ItemMovimiento
        fields = ("fecha_documento","deposito","item","tipo_movimiento","cantidad")
