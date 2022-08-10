from apps.farming.models import ActividadAgricola
from apps.inventory.models import ItemMovimiento
from apps.reports.filters import (InventarioDepositoInformeFilter,
                                  ProduccionAgricolaInformeFilter,
                                  VentaInformeFilter)
from apps.reports.tables import (InventarioDepositoInformeTable,
                                 ProduccionAgricolaInformeTable,
                                 VentaInformeTable)
from apps.sales.models import Venta
from apps.supplies import tables
from apps.supplies.filters import LibroCompraFilter
from apps.supplies.models import Compra
from core import views


# Create your views here.
class CompraInformeListView(views.ListView):
    model = Compra
    filterset_class = LibroCompraFilter
    table_class = tables.LibroCompraTable
    page_title = "Informe de compras"
    search_fields = ["comprobante", "proveedor__razon_social", "deposito__descripcion"]
    export_page_orientation = "landscape"

class VentaInformeListView(views.ListView):
    model = Venta
    filterset_class = VentaInformeFilter
    table_class = VentaInformeTable
    search_fields = ['comprobante','cliente__razon_social','deposito__descripcion']
    page_title = "Informe de ventas"
    export_page_orientation = "landscape"


class ProduccionAgricolaInformeListView(views.ListView):
    model = ActividadAgricola
    filterset_class = ProduccionAgricolaInformeFilter
    table_class = ProduccionAgricolaInformeTable
    search_fields = ['tipo_actividad_agricola__descripcion','zafra__descripcion','finca__descripcion'] 
    page_title = "Informe de actividades agricolas"
    export_page_orientation = "landscape"

class InventarioDepositoInformeListView(views.ListView):
    model = ItemMovimiento
    filterset_class = InventarioDepositoInformeFilter
    table_class = InventarioDepositoInformeTable
    search_fields = ['item__descripcion']
    page_title = "Informe de inventario deposito"
    export_page_orientation = "landscape"
