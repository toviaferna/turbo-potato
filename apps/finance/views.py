from apps.finance.filters import CuentaFilter, DistritoFilter, LocalidadFilter, PersonaFilter
from apps.finance.forms import BancoForm, CuentaForm, DepartamentoForm, DistritoForm, LocalidadForm, PaisForm, PersonaForm, TipoImpuestoForm
from apps.finance.tables import BancoTable, CuentaTable, DepartamentoTable, DistritoTable, LocalidadTable, PaisTable, PersonaTable, TipoImpuestoTable
from .models import Banco, Cuenta, Departamento, Distrito, Localidad, Pais, Persona, TipoImpuesto
from core.views import DeleteView, ListView, CreateView, UpdateView

class BancoListView(ListView):
    model = Banco
    table_class = BancoTable
    search_fields = ['descripcion',]
    update_url = 'banco_update'
    delete_url = 'banco_delete'
    create_url = 'banco_create'
    page_title = "Bancos"

class BancoCreateView(CreateView):
    form_class = BancoForm
    model = Banco
    list_url = "banco_list"
    page_title = "Agregar banco"

class BancoUpdateView(UpdateView):
    form_class = BancoForm
    model = Banco
    list_url = "banco_list"
    page_title = "Editar banco"

class BancoDeleteView(DeleteView):
    model = Banco
    list_url = "banco_list"
    page_title = "Eliminar banco"

class DepartamentoListView(ListView):
    model = Departamento
    table_class = DepartamentoTable
    search_fields = ['descripcion',]
    update_url = 'departamento_update'
    delete_url = 'departamento_delete'
    create_url = 'departamento_create'
    page_title = "Departamentos"

class DepartamentoCreateView(CreateView):
    form_class = DepartamentoForm
    model = Departamento
    list_url = "departamento_list"
    page_title = "Agregar departamento"

class DepartamentoUpdateView(UpdateView):
    form_class = DepartamentoForm
    model = Departamento
    list_url = "departamento_list"
    page_title = "Editar departamento"

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    list_url = "departamento_list"
    page_title = "Eliminar departamento"

class DistritoListView(ListView):
    model = Distrito
    table_class = DistritoTable
    filterset_class = DistritoFilter
    search_fields = ['descripcion',]
    update_url = 'distrito_update'
    delete_url = 'distrito_delete'
    create_url = 'distrito_create'
    page_title = "Distritos"

class DistritoCreateView(CreateView):
    form_class = DistritoForm
    model = Distrito
    list_url = "distrito_list"
    page_title = "Agregar distrito"

class DistritoUpdateView(UpdateView):
    form_class = DistritoForm
    model = Distrito
    list_url = "distrito_list"
    page_title = "Editar distrito"

class DistritoDeleteView(DeleteView):
    model = Distrito
    list_url = "distrito_list"
    page_title = "Eliminar distrito"

class LocalidadListView(ListView):
    model = Localidad
    table_class = LocalidadTable
    filterset_class = LocalidadFilter
    search_fields = ['descripcion',]
    update_url = 'localidad_update'
    delete_url = 'localidad_delete'
    create_url = 'localidad_create'
    page_title = "Localidades"

class LocalidadCreateView(CreateView):
    form_class = LocalidadForm
    model = Localidad
    list_url = "localidad_list"
    page_title = "Agregar localidad"

class LocalidadUpdateView(UpdateView):
    form_class = LocalidadForm
    model = Localidad
    list_url = "localidad_list"
    page_title = "Editar localidad"

class LocalidadDeleteView(DeleteView):
    model = Localidad
    list_url = "localidad_list"
    page_title = "Eliminar localidad"

class CuentaListView(ListView):
    model = Cuenta
    table_class = CuentaTable
    filterset_class = CuentaFilter
    search_fields = ['descripcion',]
    update_url = 'cuenta_update'
    delete_url = 'cuenta_delete'
    create_url = 'cuenta_create'
    page_title = "Cuentaes"

class CuentaCreateView(CreateView):
    form_class = CuentaForm
    model = Cuenta
    list_url = "cuenta_list"
    page_title = "Agregar cuenta"

class CuentaUpdateView(UpdateView):
    form_class = CuentaForm
    model = Cuenta
    list_url = "cuenta_list"
    page_title = "Editar cuenta"

class CuentaDeleteView(DeleteView):
    model = Cuenta
    list_url = "cuenta_list"
    page_title = "Eliminar cuenta"

class PaisListView(ListView):
    model = Pais
    table_class = PaisTable
    search_fields = ['descripcion',]
    update_url = 'pais_update'
    delete_url = 'pais_delete'
    create_url = 'pais_create'
    page_title = "Paises"

class PaisCreateView(CreateView):
    form_class = PaisForm
    model = Pais
    list_url = "pais_list"
    page_title = "Agregar pais"

class PaisUpdateView(UpdateView):
    form_class = PaisForm
    model = Pais
    list_url = "pais_list"
    page_title = "Editar pais"

class PaisDeleteView(DeleteView):
    model = Pais
    list_url = "pais_list"
    page_title = "Eliminar pais"

class PersonaListView(ListView):
    model = Persona
    table_class = PersonaTable
    filterset_class = PersonaFilter
    search_fields = ['razon_social',"documento"]
    update_url = 'persona_update'
    delete_url = 'persona_delete'
    create_url = 'persona_create'
    page_title = "Personas"

class PersonaCreateView(CreateView):
    form_class = PersonaForm
    model = Persona
    list_url = "persona_list"
    page_title = "Agregar persona"

class PersonaUpdateView(UpdateView):
    form_class = PersonaForm
    model = Persona
    list_url = "persona_list"
    page_title = "Editar persona"

class PersonaDeleteView(DeleteView):
    model = Persona
    list_url = "persona_list"
    page_title = "Eliminar persona"

class TipoImpuestoListView(ListView):
    model = TipoImpuesto
    table_class = TipoImpuestoTable
    search_fields = ['descripcion',]
    update_url = 'impuesto_update'
    delete_url = 'impuesto_delete'
    create_url = 'impuesto_create'
    page_title = "Tipos de impuestos"

class TipoImpuestoCreateView(CreateView):
    form_class = TipoImpuestoForm
    model = TipoImpuesto
    list_url = "impuesto_list"
    page_title = "Agregar tipo de impuesto"

class TipoImpuestoUpdateView(UpdateView):
    form_class = TipoImpuestoForm
    model = TipoImpuesto
    list_url = "impuesto_list"
    page_title = "Editar tipo de impuesto"

class TipoImpuestoDeleteView(DeleteView):
    model = TipoImpuesto
    list_url = "impuesto_list"
    page_title = "Eliminar tipo de impuesto"
