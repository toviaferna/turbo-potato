from apps.farming.filters import (PlanActividadZafraFilter,
                                  TipoActividadAgricolaFilter, ZafraFilter)
from apps.farming.forms import (AcopioForm, ActividadAgricolaForm,
                                CalificacionAgricolaForm, ContratoForm,
                                FincaForm, LoteForm, MaquinariaAgricolaForm,
                                PlanActividadZafraForm,
                                TipoActividadAgricolaForm,
                                TipoMaquinariaAgricolaForm, ZafraForm)
from apps.farming.inlines import (AcopioCalificacionDetalleInline,
                                  AcopioDetalleInline,
                                  ActividadAgricolaItemDetalleInline,
                                  ActividadAgricolaMaquinariaDetalleInline,
                                  PlanActividadZafraDetalleInline)
from apps.farming.tables import (AcopioTable, ActividadAgricolaTable,
                                 CalificacionAgricolaTable, ContratoTable,
                                 FincaTable, LoteTable,
                                 MaquinariaAgricolaTable,
                                 PlanActividadZafraTable,
                                 TipoActividadAgricolaTable,
                                 TipoMaquinariaAgricolaTable, ZafraTable)
from core.views import (AnnulledView, CreateView, DeleteView, ListView,
                        UpdateView)

from .models import (Acopio, ActividadAgricola, CalificacionAgricola, Contrato,
                     Finca, Lote, MaquinariaAgricola, PlanActividadZafra,
                     TipoActividadAgricola, TipoMaquinariaAgricola, Zafra)


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

class PlanActividadZafraListView(ListView):
    model = PlanActividadZafra
    table_class = PlanActividadZafraTable
    filterset_class = PlanActividadZafraFilter
    search_fields = ['zafra__descripcion', 'observacion']
    update_url = 'plan_actividad_zafra_update'
    create_url = 'plan_actividad_zafra_create'
    delete_url = None

class PlanActividadZafraCreateView(CreateView):
    model = PlanActividadZafra
    form_class = PlanActividadZafraForm
    inlines = [PlanActividadZafraDetalleInline]
    list_url = "plan_actividad_zafra_list"


class PlanActividadZafraUpdateView(UpdateView):
    model = PlanActividadZafra
    form_class = PlanActividadZafraForm
    inlines = [PlanActividadZafraDetalleInline]
    list_url = "plan_actividad_zafra_list"

class ContratoListView(ListView):
    model = Contrato
    table_class = ContratoTable
    search_fields = ['descripcion', 'item__descripcion']
    update_url = 'contrato_update'
    delete_url = 'contrato_delete'
    create_url = 'contrato_create'

class ContratoCreateView(CreateView):
    form_class = ContratoForm
    model = Contrato
    list_url = "contrato_list"

class ContratoDeleteView(DeleteView):
    model = Contrato
    list_url = "contrato_list"

class AcopioListView(ListView):
    model = Acopio
    table_class = AcopioTable
    search_fields = ['zafra__descripcion', 'comprobante','deposito__descripcion']
    update_url = 'acopio_update'
    delete_url = 'acopio_delete'
    create_url = 'acopio_create'


class AcopioCreateView(CreateView):
    model = Acopio
    form_class = AcopioForm
    inlines = [AcopioDetalleInline,AcopioCalificacionDetalleInline]
    list_url = "acopio_list"

    def run_form_extra_validation(self, form, inlines):
        acopio_detalle = inlines[0]
        total_peso = 0
        existe_registro = False
        peso_encabezado =  (form.cleaned_data.get('peso_bruto') + form.cleaned_data.get('peso_bonificacion')) - (form.cleaned_data.get('peso_tara') + form.cleaned_data.get('peso_descuento'))
        
        for f in acopio_detalle:
            total_peso = total_peso + f.cleaned_data.get('peso')
            existe_registro = True

        if existe_registro == False or total_peso == 0 or total_peso is None:
            form.add_error(None, 'Registre al menos un detalle del acopio')
        
        if peso_encabezado != total_peso:  
            form.add_error('peso_bruto', 'El neto (Peso Bruto + Peso Bonificacion ) - ( Peso Tara + Peso Descuento) no es igual a los detalles cargados')

class AcopioUpdateView(UpdateView):
    model = Acopio
    form_class = AcopioForm
    list_url = "acopio_list"
    inlines = [AcopioDetalleInline,AcopioCalificacionDetalleInline]

class AcopioAnnulledView(AnnulledView):
    model = Acopio
    list_url = "acopio_list"
    mensaje_anulacion = "El acopio ya fue anulado."

class ActividadAgricolaListView(ListView):
    model = ActividadAgricola
    table_class = ActividadAgricolaTable
    search_fields = ['zafra__descripcion','finca__descripcion','lote__descripcion', 'empleado__razon_social','deposito__descripcion']
    update_url = None
    delete_url = 'actividad_agricola_delete'
    create_url = 'actividad_agricola_create'


class ActividadAgricolaCreateView(CreateView):
    model = ActividadAgricola
    form_class = ActividadAgricolaForm
    inlines = [ActividadAgricolaMaquinariaDetalleInline,ActividadAgricolaItemDetalleInline]
    list_url = "actividad_agricola_list"
    
    def run_form_extra_validation(self, form, inlines):
        """ ejecutar validaciones adicionales de formularios """
        detalle_maquinaria = inlines[0] 
        detalle_item = inlines[1]

        cantidad_ha_maquinaria = 0

        for f in detalle_maquinaria:
           cantidad_maquinaria = f.cleaned_data.get('ha_trabajada')
           if cantidad_maquinaria is None:
                cantidad_maquinaria = 0
           cantidad_ha_maquinaria += cantidad_maquinaria
               
        if (cantidad_ha_maquinaria != form.cleaned_data.get('cantidad_trabajada')) and form.cleaned_data.get('es_servicio_contratado') == False and cantidad_ha_maquinaria > 0 :
            form.add_error(None, 'La cantidad de HA trabajada debe ser igual a la cantidad de HA trabajada por las maquinarias')

class ActividadAgricolaAnnulledView(AnnulledView):
    model = ActividadAgricola
    template_name = 'inventory/anular.html'
    list_url = "actividad_agricola_list"
    mensaje_anulacion = "La Actividad Agrícola ya fue anulado."
