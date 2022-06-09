from apps.farming.filters import TipoActividadAgricolaFilter, ZafraFilter
from apps.farming.forms import CalificacionAgricolaForm, FincaForm, LoteForm, MaquinariaAgricolaForm, TipoActividadAgricolaForm, TipoMaquinariaAgricolaForm, ZafraForm
from apps.farming.tables import CalificacionAgricolaTable, FincaTable, LoteTable, MaquinariaAgricolaTable, TipoActividadAgricolaTable, TipoMaquinariaAgricolaTable, ZafraTable
from core.views import CreateView, DeleteView, ListView, UpdateView

from .models import CalificacionAgricola, Finca, Lote, MaquinariaAgricola, TipoActividadAgricola, TipoMaquinariaAgricola, Zafra


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

class ZafraListView(ListView):
    model = Zafra
    table_class = ZafraTable
    filterset_class = ZafraFilter
    search_fields = ['descripcion', 'item__descripcion']
    update_url = 'zafra_update'
    delete_url = 'zafra_delete'
    create_url = 'zafra_create'

class ZafraCreateView(CreateView):
    form_class = ZafraForm
    model = Zafra
    list_url = "zafra_list"

class ZafraUpdateView(UpdateView):
    form_class = ZafraForm
    model = Zafra
    list_url = "zafra_list"

class ZafraDeleteView(DeleteView):
    model = Zafra
    list_url = "zafra_list"

class LoteListView(ListView):
    model = Lote
    table_class = LoteTable
    search_fields = ['descripcion', 'item__descripcion']
    update_url = 'lote_update'
    delete_url = 'lote_delete'
    create_url = 'lote_create'

class LoteCreateView(CreateView):
    form_class = LoteForm
    model = Lote
    list_url = "lote_list"

class LoteUpdateView(UpdateView):
    form_class = LoteForm
    model = Lote
    list_url = "lote_list"

class LoteDeleteView(DeleteView):
    model = Lote
    list_url = "lote_list"
