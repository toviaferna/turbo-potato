from apps.inventory.filters import DepositoFilter, ItemFilter
from apps.inventory.forms import (CategoriaForm, DepositoForm, ItemForm,
                                  MarcaForm, TipoItemForm)
from apps.inventory.tables import (CategoriaTable, DepositoTable, ItemTable,
                                   MarcaTable, TipoItemTable)
from core.views import CreateView, DeleteView, ListView, UpdateView

from .models import Categoria, Deposito, Item, Marca, TipoItem


# FINCA
class MarcaListView(ListView):
    model = Marca
    table_class = MarcaTable
    search_fields = ['descripcion',]
    update_url = 'marca_update'
    delete_url = 'marca_delete'
    create_url = 'marca_create'

class MarcaCreateView(CreateView):
    form_class = MarcaForm
    model = Marca
    list_url = "marca_list"

class MarcaUpdateView(UpdateView):
    form_class = MarcaForm
    model = Marca
    list_url = "marca_list"

class MarcaDeleteView(DeleteView):
    model = Marca
    list_url = "marca_list"

class CategoriaListView(ListView):
    model = Categoria
    table_class = CategoriaTable
    search_fields = ['descripcion',]
    update_url = 'categoria_update'
    delete_url = 'categoria_delete'
    create_url = 'categoria_create'

class CategoriaCreateView(CreateView):
    form_class = CategoriaForm
    model = Categoria
    list_url = "categoria_list"

class CategoriaUpdateView(UpdateView):
    form_class = CategoriaForm
    model = Categoria
    list_url = "categoria_list"

class CategoriaDeleteView(DeleteView):
    model = Categoria
    list_url = "categoria_list"

class DepositoListView(ListView):
    model = Deposito
    table_class = DepositoTable
    search_fields = ['descripcion',]
    filterset_class = DepositoFilter
    update_url = 'deposito_update'
    delete_url = 'deposito_delete'
    create_url = 'deposito_create'

class DepositoCreateView(CreateView):
    form_class = DepositoForm
    model = Deposito
    list_url = "deposito_list"

class DepositoUpdateView(UpdateView):
    form_class = DepositoForm
    model = Deposito
    list_url = "deposito_list"

class DepositoDeleteView(DeleteView):
    model = Deposito
    list_url = "deposito_list"

class ItemListView(ListView):
    model = Item
    table_class = ItemTable
    filterset_class = ItemFilter
    search_fields = ['descripcion',]
    update_url = 'item_update'
    delete_url = 'item_delete'
    create_url = 'item_create'

class ItemCreateView(CreateView):
    form_class = ItemForm
    model = Item
    list_url = "item_list"

class ItemUpdateView(UpdateView):
    form_class = ItemForm
    model = Item
    list_url = "item_list"

class ItemDeleteView(DeleteView):
    model = Item
    list_url = "item_list"

class TipoItemListView(ListView):
    model = TipoItem
    table_class = TipoItemTable
    search_fields = ['descripcion',]
    update_url = 'tipo_item_update'
    delete_url = 'tipo_item_delete'
    create_url = 'tipo_item_create'

class TipoItemCreateView(CreateView):
    form_class = TipoItemForm
    model = TipoItem
    list_url = "tipo_item_list"

class TipoItemUpdateView(UpdateView):
    form_class = TipoItemForm
    model = TipoItem
    list_url = "tipo_item_list"

class TipoItemDeleteView(DeleteView):
    model = TipoItem
    list_url = "tipo_item_list"
