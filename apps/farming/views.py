from apps.farming.forms import FincaForm
from apps.farming.tables import FincaTable
from core.views import CreateView, DeleteView, ListView, UpdateView

from .models import Finca


# FINCA
class FincaListView(ListView):
    model = Finca
    table_class = FincaTable
    search_fields = ['descripcion','ubicacion']
    update_url = 'finca_update'
    delete_url = 'finca_delete'
    create_url = 'finca_create'
    page_title = "Fincas"

class FincaCreateView(CreateView):
    form_class = FincaForm
    model = Finca
    list_url = "finca_list"
    page_title = "Agregar fincas"

class FincaUpdateView(UpdateView):
    form_class = FincaForm
    model = Finca
    list_url = "finca_list"
    page_title = "Editar fincas"

class FincaDeleteView(DeleteView):
    model = Finca
    list_url = "finca_list"
    page_title = "Eliminar fincas"
