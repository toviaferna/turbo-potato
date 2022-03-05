from apps.supplies.forms import MarcaForm
from apps.supplies.tables import MarcaTable
from .models import Marca
from core.views import DeleteView, ListView, CreateView, UpdateView
# FINCA
class MarcaListView(ListView):
    model = Marca
    table_class = MarcaTable
    search_fields = ['descripcion',]
    update_url = 'marca_update'
    delete_url = 'marca_delete'
    create_url = 'marca_create'
    page_title = "Marcas"

class MarcaCreateView(CreateView):
    form_class = MarcaForm
    model = Marca
    list_url = "marca_list"
    page_title = "Agregar marcas"

class MarcaUpdateView(UpdateView):
    form_class = MarcaForm
    model = Marca
    list_url = "marca_list"
    page_title = "Editar marcas"

class MarcaDeleteView(DeleteView):
    model = Marca
    list_url = "marca_list"
    page_title = "Eliminar marcas"
