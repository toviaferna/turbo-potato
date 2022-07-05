from apps.sales.filters import AperturaCajaFilter
from apps.sales.forms import AperturaCajaCreateForm
from apps.sales.models import AperturaCaja
from apps.sales.tables import AperturaCajaTable
from core.views import CreateView, ListView


# Create your views here.
class AperturaCajaListView(ListView):
    model = AperturaCaja
    table_class = AperturaCajaTable
    filterset_class = AperturaCajaFilter
    search_fields = ['empleado__razon_social','observacion']
    update_url = None
    create_url = "apertura_caja_create"#'apertura_caja_create'
    delete_url = None#'apertura_caja_delete'

class AperturaCajaCreateView(CreateView):
    form_class = AperturaCajaCreateForm
    model = AperturaCaja
    list_url = "apertura_caja_list"
