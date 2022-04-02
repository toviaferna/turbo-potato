from apps.finance.filters import (CuentaFilter, DistritoFilter,
                                  LocalidadFilter, PersonaFilter)
from apps.finance.forms import (BancoForm, CuentaForm, DepartamentoForm,
                                DistritoForm, LocalidadForm, PaisForm,
                                PersonaForm, TipoImpuestoForm)
from apps.finance.tables import (BancoTable, CuentaTable, DepartamentoTable,
                                 DistritoTable, LocalidadTable, PaisTable,
                                 PersonaTable, TipoImpuestoTable)
from core.views import CreateView, DeleteView, ListView, UpdateView

from .models import (Banco, Cuenta, Departamento, Distrito, Localidad, Pais,
                     Persona, TipoImpuesto)


class BancoListView(ListView):
    model = Banco
    table_class = BancoTable
    search_fields = ['descripcion',]
    update_url = 'banco_update'
    delete_url = 'banco_delete'
    create_url = 'banco_create'

class BancoCreateView(CreateView):
    form_class = BancoForm
    model = Banco
    list_url = "banco_list"

class BancoUpdateView(UpdateView):
    form_class = BancoForm
    model = Banco
    list_url = "banco_list"

class BancoDeleteView(DeleteView):
    model = Banco
    list_url = "banco_list"

class DepartamentoListView(ListView):
    model = Departamento
    table_class = DepartamentoTable
    search_fields = ['descripcion',]
    update_url = 'departamento_update'
    delete_url = 'departamento_delete'
    create_url = 'departamento_create'

class DepartamentoCreateView(CreateView):
    form_class = DepartamentoForm
    model = Departamento
    list_url = "departamento_list"

class DepartamentoUpdateView(UpdateView):
    form_class = DepartamentoForm
    model = Departamento
    list_url = "departamento_list"

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    list_url = "departamento_list"

class DistritoListView(ListView):
    model = Distrito
    table_class = DistritoTable
    filterset_class = DistritoFilter
    search_fields = ['descripcion',]
    update_url = 'distrito_update'
    delete_url = 'distrito_delete'
    create_url = 'distrito_create'

class DistritoCreateView(CreateView):
    form_class = DistritoForm
    model = Distrito
    list_url = "distrito_list"

class DistritoUpdateView(UpdateView):
    form_class = DistritoForm
    model = Distrito
    list_url = "distrito_list"

class DistritoDeleteView(DeleteView):
    model = Distrito
    list_url = "distrito_list"

class LocalidadListView(ListView):
    model = Localidad
    table_class = LocalidadTable
    filterset_class = LocalidadFilter
    search_fields = ['descripcion',]
    update_url = 'localidad_update'
    delete_url = 'localidad_delete'
    create_url = 'localidad_create'

class LocalidadCreateView(CreateView):
    form_class = LocalidadForm
    model = Localidad
    list_url = "localidad_list"

class LocalidadUpdateView(UpdateView):
    form_class = LocalidadForm
    model = Localidad
    list_url = "localidad_list"

class LocalidadDeleteView(DeleteView):
    model = Localidad
    list_url = "localidad_list"

class CuentaListView(ListView):
    model = Cuenta
    table_class = CuentaTable
    filterset_class = CuentaFilter
    search_fields = ['descripcion',]
    update_url = 'cuenta_update'
    delete_url = 'cuenta_delete'
    create_url = 'cuenta_create'

class CuentaCreateView(CreateView):
    form_class = CuentaForm
    model = Cuenta
    list_url = "cuenta_list"

class CuentaUpdateView(UpdateView):
    form_class = CuentaForm
    model = Cuenta
    list_url = "cuenta_list"

class CuentaDeleteView(DeleteView):
    model = Cuenta
    list_url = "cuenta_list"

class PaisListView(ListView):
    model = Pais
    table_class = PaisTable
    search_fields = ['descripcion',]
    update_url = 'pais_update'
    delete_url = 'pais_delete'
    create_url = 'pais_create'

class PaisCreateView(CreateView):
    form_class = PaisForm
    model = Pais
    list_url = "pais_list"

class PaisUpdateView(UpdateView):
    form_class = PaisForm
    model = Pais
    list_url = "pais_list"

class PaisDeleteView(DeleteView):
    model = Pais
    list_url = "pais_list"

class PersonaListView(ListView):
    model = Persona
    table_class = PersonaTable
    filterset_class = PersonaFilter
    search_fields = ['razon_social',"documento"]
    update_url = 'persona_update'
    delete_url = 'persona_delete'
    create_url = 'persona_create'

class PersonaCreateView(CreateView):
    form_class = PersonaForm
    model = Persona
    list_url = "persona_list"

class PersonaUpdateView(UpdateView):
    form_class = PersonaForm
    model = Persona
    list_url = "persona_list"

class PersonaDeleteView(DeleteView):
    model = Persona
    list_url = "persona_list"

class TipoImpuestoListView(ListView):
    model = TipoImpuesto
    table_class = TipoImpuestoTable
    search_fields = ['descripcion',]
    update_url = 'impuesto_update'
    delete_url = 'impuesto_delete'
    create_url = 'impuesto_create'

class TipoImpuestoCreateView(CreateView):
    form_class = TipoImpuestoForm
    model = TipoImpuesto
    list_url = "impuesto_list"

class TipoImpuestoUpdateView(UpdateView):
    form_class = TipoImpuestoForm
    model = TipoImpuesto
    list_url = "impuesto_list"

class TipoImpuestoDeleteView(DeleteView):
    model = TipoImpuesto
    list_url = "impuesto_list"
