from apps.sales.filters import AperturaCajaFilter
from apps.sales.models import AperturaCaja
from apps.sales.tables import AperturaCajaTable
from core.views import ListView
# Create your views here.
class AperturaCajaListView(ListView):
    model = AperturaCaja
    table_class = AperturaCajaTable
    filterset_class = AperturaCajaFilter
    search_fields = ['empleado__razon_social','observacion']
    update_url = None
    create_url = None#'apertura_caja_create'
    delete_url = None#'apertura_caja_delete'