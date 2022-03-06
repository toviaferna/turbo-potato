from apps.inventory.filters import DepositoFilter, ItemFilter
from apps.inventory.forms import CategoriaForm, DepositoForm, ItemForm, MarcaForm, TipoItemForm
from apps.inventory.tables import CategoriaTable, DepositoTable, ItemTable, MarcaTable, TipoItemTable
from .models import Categoria, Deposito, Item, Marca, TipoItem
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
    page_title = "Agregar marca"

class MarcaUpdateView(UpdateView):
    form_class = MarcaForm
    model = Marca
    list_url = "marca_list"
    page_title = "Editar marca"

class MarcaDeleteView(DeleteView):
    model = Marca
    list_url = "marca_list"
    page_title = "Eliminar marca"

class CategoriaListView(ListView):
    model = Categoria
    table_class = CategoriaTable
    search_fields = ['descripcion',]
    update_url = 'categoria_update'
    delete_url = 'categoria_delete'
    create_url = 'categoria_create'
    page_title = "Categorias"

class CategoriaCreateView(CreateView):
    form_class = CategoriaForm
    model = Categoria
    list_url = "categoria_list"
    page_title = "Agregar categoria"

class CategoriaUpdateView(UpdateView):
    form_class = CategoriaForm
    model = Categoria
    list_url = "categoria_list"
    page_title = "Editar categoria"

class CategoriaDeleteView(DeleteView):
    model = Categoria
    list_url = "categoria_list"
    page_title = "Eliminar categoria"

class DepositoListView(ListView):
    model = Deposito
    table_class = DepositoTable
    search_fields = ['descripcion',]
    filterset_class = DepositoFilter
    update_url = 'deposito_update'
    delete_url = 'deposito_delete'
    create_url = 'deposito_create'
    page_title = "Depositos"

class DepositoCreateView(CreateView):
    form_class = DepositoForm
    model = Deposito
    list_url = "deposito_list"
    page_title = "Agregar deposito"

class DepositoUpdateView(UpdateView):
    form_class = DepositoForm
    model = Deposito
    list_url = "deposito_list"
    page_title = "Editar deposito"

class DepositoDeleteView(DeleteView):
    model = Deposito
    list_url = "deposito_list"
    page_title = "Eliminar deposito"

class ItemListView(ListView):
    model = Item
    table_class = ItemTable
    filterset_class = ItemFilter
    search_fields = ['descripcion',]
    update_url = 'item_update'
    delete_url = 'item_delete'
    create_url = 'item_create'
    page_title = "Items"

class ItemCreateView(CreateView):
    form_class = ItemForm
    model = Item
    list_url = "item_list"
    page_title = "Agregar item"

class ItemUpdateView(UpdateView):
    form_class = ItemForm
    model = Item
    list_url = "item_list"
    page_title = "Editar item"

class ItemDeleteView(DeleteView):
    model = Item
    list_url = "item_list"
    page_title = "Eliminar item"

class TipoItemListView(ListView):
    model = TipoItem
    table_class = TipoItemTable
    search_fields = ['descripcion',]
    update_url = 'tipo_item_update'
    delete_url = 'tipo_item_delete'
    create_url = 'tipo_item_create'
    page_title = "Tipo de Items"

class TipoItemCreateView(CreateView):
    form_class = TipoItemForm
    model = TipoItem
    list_url = "tipo_item_list"
    page_title = "Agregar tipo de item"

class TipoItemUpdateView(UpdateView):
    form_class = TipoItemForm
    model = TipoItem
    list_url = "tipo_item_list"
    page_title = "Editar tipo de item"

class TipoItemDeleteView(DeleteView):
    model = TipoItem
    list_url = "tipo_item_list"
    page_title = "Eliminar tipo de item"
