from apps.finance import filters, forms, models, tables
from core import views


class BancoListView(views.ListView):
    model = models.Banco
    table_class = tables.BancoTable
    search_fields = ['descripcion',]
    update_url = 'banco_update'
    delete_url = 'banco_delete'
    create_url = 'banco_create'

class BancoCreateView(views.CreateView):
    form_class = forms.BancoForm
    model = models.Banco
    list_url = "banco_list"

class BancoUpdateView(views.UpdateView):
    form_class = forms.BancoForm
    model = models.Banco
    list_url = "banco_list"

class BancoDeleteView(views.DeleteView):
    model = models.Banco
    list_url = "banco_list"

class DepartamentoListView(views.ListView):
    model = models.Departamento
    table_class = tables.DepartamentoTable
    search_fields = ['descripcion',]
    update_url = 'departamento_update'
    delete_url = 'departamento_delete'
    create_url = 'departamento_create'

class DepartamentoCreateView(views.CreateView):
    form_class = forms.DepartamentoForm
    model = models.Departamento
    list_url = "departamento_list"

class DepartamentoUpdateView(views.UpdateView):
    form_class = forms.DepartamentoForm
    model = models.Departamento
    list_url = "departamento_list"

class DepartamentoDeleteView(views.DeleteView):
    model = models.Departamento
    list_url = "departamento_list"

class DistritoListView(views.ListView):
    model = models.Distrito
    table_class = tables.DistritoTable
    filterset_class = filters.DistritoFilter
    search_fields = ['descripcion',]
    update_url = 'distrito_update'
    delete_url = 'distrito_delete'
    create_url = 'distrito_create'

class DistritoCreateView(views.CreateView):
    form_class = forms.DistritoForm
    model = models.Distrito
    list_url = "distrito_list"

class DistritoUpdateView(views.UpdateView):
    form_class = forms.DistritoForm
    model = models.Distrito
    list_url = "distrito_list"

class DistritoDeleteView(views.DeleteView):
    model = models.Distrito
    list_url = "distrito_list"

class LocalidadListView(views.ListView):
    model = models.Localidad
    table_class = tables.LocalidadTable
    filterset_class = filters.LocalidadFilter
    search_fields = ['descripcion',]
    update_url = 'localidad_update'
    delete_url = 'localidad_delete'
    create_url = 'localidad_create'

class LocalidadCreateView(views.CreateView):
    form_class = forms.LocalidadForm
    model = models.Localidad
    list_url = "localidad_list"

class LocalidadUpdateView(views.UpdateView):
    form_class = forms.LocalidadForm
    model = models.Localidad
    list_url = "localidad_list"

class LocalidadDeleteView(views.DeleteView):
    model = models.Localidad
    list_url = "localidad_list"

class CuentaListView(views.ListView):
    model = models.Cuenta
    table_class = tables.CuentaTable
    filterset_class = filters.CuentaFilter
    search_fields = ['descripcion',]
    update_url = 'cuenta_update'
    delete_url = 'cuenta_delete'
    create_url = 'cuenta_create'

class CuentaCreateView(views.CreateView):
    form_class = forms.CuentaForm
    model = models.Cuenta
    list_url = "cuenta_list"

class CuentaUpdateView(views.UpdateView):
    form_class = forms.CuentaForm
    model = models.Cuenta
    list_url = "cuenta_list"

class CuentaDeleteView(views.DeleteView):
    model = models.Cuenta
    list_url = "cuenta_list"

class PaisListView(views.ListView):
    model = models.Pais
    table_class = tables.PaisTable
    search_fields = ['descripcion',]
    update_url = 'pais_update'
    delete_url = 'pais_delete'
    create_url = 'pais_create'

class PaisCreateView(views.CreateView):
    form_class = forms.PaisForm
    model = models.Pais
    list_url = "pais_list"

class PaisUpdateView(views.UpdateView):
    form_class = forms.PaisForm
    model = models.Pais
    list_url = "pais_list"

class PaisDeleteView(views.DeleteView):
    model = models.Pais
    list_url = "pais_list"

class PersonaListView(views.ListView):
    model = models.Persona
    table_class = tables.PersonaTable
    filterset_class = filters.PersonaFilter
    search_fields = ['razon_social',"documento"]
    update_url = 'persona_update'
    delete_url = 'persona_delete'
    create_url = 'persona_create'


class PersonaCreateView(views.CreateView):
    form_class = forms.PersonaForm
    model = models.Persona
    list_url = "persona_list"
    class Media:
        js = ("assets/js/documento.js",)

class PersonaUpdateView(views.UpdateView):
    form_class = forms.PersonaForm
    model = models.Persona
    list_url = "persona_list"

class PersonaDeleteView(views.DeleteView):
    model = models.Persona
    list_url = "persona_list"

class TipoImpuestoListView(views.ListView):
    model = models.TipoImpuesto
    table_class = tables.TipoImpuestoTable
    search_fields = ['descripcion',]
    update_url = 'impuesto_update'
    delete_url = 'impuesto_delete'
    create_url = 'impuesto_create'

class TipoImpuestoCreateView(views.CreateView):
    form_class = forms.TipoImpuestoForm
    model = models.TipoImpuesto
    list_url = "impuesto_list"

class TipoImpuestoUpdateView(views.UpdateView):
    form_class = forms.TipoImpuestoForm
    model = models.TipoImpuesto
    list_url = "impuesto_list"

class TipoImpuestoDeleteView(views.DeleteView):
    model = models.TipoImpuesto
    list_url = "impuesto_list"
