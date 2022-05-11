from apps.farming.filters import TipoActividadAgricolaFilter
from apps.farming.forms import CalificacionAgricolaForm, FincaForm, MaquinariaAgricolaForm, TipoActividadAgricolaForm, TipoMaquinariaAgricolaForm
from apps.farming.tables import CalificacionAgricolaTable, FincaTable, MaquinariaAgricolaTable, TipoActividadAgricolaTable, TipoMaquinariaAgricolaTable
from core.views import CreateView, DeleteView, ListView, UpdateView

from .models import CalificacionAgricola, Finca, MaquinariaAgricola, TipoActividadAgricola, TipoMaquinariaAgricola


# FINCA
class FincaListView(ListView):
    model = Finca
    table_class = FincaTable
    search_fields = ['descripcion','ubicacion']
    update_url = 'finca_update'
    delete_url = 'finca_delete'
    create_url = 'finca_create'

class FincaCreateView(CreateView):
    form_class = FincaForm
    model = Finca
    list_url = "finca_list"

class FincaUpdateView(UpdateView):
    form_class = FincaForm
    model = Finca
    list_url = "finca_list"

class FincaDeleteView(DeleteView):
    model = Finca
    list_url = "finca_list"


class CalificacionAgricolaListView(ListView):
    model = CalificacionAgricola
    table_class = CalificacionAgricolaTable
    search_fields = ['descripcion',]
    update_url = 'calificacion_agricola_update'
    delete_url = 'calificacion_agricola_delete'
    create_url = 'calificacion_agricola_create'

class CalificacionAgricolaCreateView(CreateView):
    form_class = CalificacionAgricolaForm
    model = CalificacionAgricola
    list_url = "calificacion_agricola_list"

class CalificacionAgricolaUpdateView(UpdateView):
    form_class = CalificacionAgricolaForm
    model = CalificacionAgricola
    list_url = "calificacion_agricola_list"

class CalificacionAgricolaDeleteView(DeleteView):
    model = CalificacionAgricola
    list_url = "calificacion_agricola_list"

class TipoActividadAgricolaListView(ListView):
    model = TipoActividadAgricola
    table_class = TipoActividadAgricolaTable
    filterset_class = TipoActividadAgricolaFilter
    search_fields = ['descripcion',]
    update_url = 'tipo_actividad_agricola_update'
    delete_url = 'tipo_actividad_agricola_delete'
    create_url = 'tipo_actividad_agricola_create'

class TipoActividadAgricolaCreateView(CreateView):
    form_class = TipoActividadAgricolaForm
    model = TipoActividadAgricola
    list_url = "tipo_actividad_agricola_list"

class TipoActividadAgricolaUpdateView(UpdateView):
    form_class = TipoActividadAgricolaForm
    model = TipoActividadAgricola
    list_url = "tipo_actividad_agricola_list"

class TipoActividadAgricolaDeleteView(DeleteView):
    model = TipoActividadAgricola
    list_url = "tipo_actividad_agricola_list"

class TipoMaquinariaAgricolaListView(ListView):
    model = TipoMaquinariaAgricola
    table_class = TipoMaquinariaAgricolaTable
    search_fields = ['descripcion',]
    update_url = 'tipo_maquinaria_agricola_update'
    delete_url = 'tipo_maquinaria_agricola_delete'
    create_url = 'tipo_maquinaria_agricola_create'

class TipoMaquinariaAgricolaCreateView(CreateView):
    form_class = TipoMaquinariaAgricolaForm
    model = TipoMaquinariaAgricola
    list_url = "tipo_maquinaria_agricola_list"

class TipoMaquinariaAgricolaUpdateView(UpdateView):
    form_class = TipoMaquinariaAgricolaForm
    model = TipoMaquinariaAgricola
    list_url = "tipo_maquinaria_agricola_list"

class TipoMaquinariaAgricolaDeleteView(DeleteView):
    model = TipoMaquinariaAgricola
    list_url = "tipo_maquinaria_agricola_list"
    
class MaquinariaAgricolaListView(ListView):
    model = MaquinariaAgricola
    table_class = MaquinariaAgricolaTable
    search_fields = ['descripcion',]
    update_url = 'maquinaria_agricola_update'
    delete_url = 'maquinaria_agricola_delete'
    create_url = 'maquinaria_agricola_create'

class MaquinariaAgricolaCreateView(CreateView):
    form_class = MaquinariaAgricolaForm
    model = MaquinariaAgricola
    list_url = "maquinaria_agricola_list"

class MaquinariaAgricolaUpdateView(UpdateView):
    form_class = MaquinariaAgricolaForm
    model = MaquinariaAgricola
    list_url = "maquinaria_agricola_list"

class MaquinariaAgricolaDeleteView(DeleteView):
    model = MaquinariaAgricola
    list_url = "maquinaria_agricola_list"
