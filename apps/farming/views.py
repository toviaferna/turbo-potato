from apps.farming import filters, forms, inlines, models, tables
from core import views
from django.db.models import F, Sum


# FINCA
class FincaListView(views.ListView):
    model = models.Finca
    table_class = tables.FincaTable
    search_fields = ["descripcion", "ubicacion"]
    update_url = "finca_update"
    delete_url = "finca_delete"
    create_url = "finca_create"


class FincaCreateView(views.CreateView):
    form_class = forms.FincaForm
    model = models.Finca
    list_url = "finca_list"


class FincaUpdateView(views.UpdateView):
    form_class = forms.FincaForm
    model = models.Finca
    list_url = "finca_list"


class FincaDeleteView(views.DeleteView):
    model = models.Finca
    list_url = "finca_list"


class CalificacionAgricolaListView(views.ListView):
    model = models.CalificacionAgricola
    table_class = tables.CalificacionAgricolaTable
    search_fields = [
        "descripcion",
    ]
    update_url = "calificacion_agricola_update"
    delete_url = "calificacion_agricola_delete"
    create_url = "calificacion_agricola_create"


class CalificacionAgricolaCreateView(views.CreateView):
    form_class = forms.CalificacionAgricolaForm
    model = models.CalificacionAgricola
    list_url = "calificacion_agricola_list"


class CalificacionAgricolaUpdateView(views.UpdateView):
    form_class = forms.CalificacionAgricolaForm
    model = models.CalificacionAgricola
    list_url = "calificacion_agricola_list"


class CalificacionAgricolaDeleteView(views.DeleteView):
    model = models.CalificacionAgricola
    list_url = "calificacion_agricola_list"


class TipoActividadAgricolaListView(views.ListView):
    model = models.TipoActividadAgricola
    table_class = tables.TipoActividadAgricolaTable
    filterset_class = filters.TipoActividadAgricolaFilter
    search_fields = [
        "descripcion",
    ]
    update_url = "tipo_actividad_agricola_update"
    delete_url = "tipo_actividad_agricola_delete"
    create_url = "tipo_actividad_agricola_create"


class TipoActividadAgricolaCreateView(views.CreateView):
    form_class = forms.TipoActividadAgricolaForm
    model = models.TipoActividadAgricola
    list_url = "tipo_actividad_agricola_list"


class TipoActividadAgricolaUpdateView(views.UpdateView):
    form_class = forms.TipoActividadAgricolaForm
    model = models.TipoActividadAgricola
    list_url = "tipo_actividad_agricola_list"


class TipoActividadAgricolaDeleteView(views.DeleteView):
    model = models.TipoActividadAgricola
    list_url = "tipo_actividad_agricola_list"


class TipoMaquinariaAgricolaListView(views.ListView):
    model = models.TipoMaquinariaAgricola
    table_class = tables.TipoMaquinariaAgricolaTable
    search_fields = [
        "descripcion",
    ]
    update_url = "tipo_maquinaria_agricola_update"
    delete_url = "tipo_maquinaria_agricola_delete"
    create_url = "tipo_maquinaria_agricola_create"


class TipoMaquinariaAgricolaCreateView(views.CreateView):
    form_class = forms.TipoMaquinariaAgricolaForm
    model = models.TipoMaquinariaAgricola
    list_url = "tipo_maquinaria_agricola_list"


class TipoMaquinariaAgricolaUpdateView(views.UpdateView):
    form_class = forms.TipoMaquinariaAgricolaForm
    model = models.TipoMaquinariaAgricola
    list_url = "tipo_maquinaria_agricola_list"


class TipoMaquinariaAgricolaDeleteView(views.DeleteView):
    model = models.TipoMaquinariaAgricola
    list_url = "tipo_maquinaria_agricola_list"


class MaquinariaAgricolaListView(views.ListView):
    model = models.MaquinariaAgricola
    table_class = tables.MaquinariaAgricolaTable
    search_fields = [
        "descripcion",
    ]
    update_url = "maquinaria_agricola_update"
    delete_url = "maquinaria_agricola_delete"
    create_url = "maquinaria_agricola_create"


class MaquinariaAgricolaCreateView(views.CreateView):
    form_class = forms.MaquinariaAgricolaForm
    model = models.MaquinariaAgricola
    list_url = "maquinaria_agricola_list"


class MaquinariaAgricolaUpdateView(views.UpdateView):
    form_class = forms.MaquinariaAgricolaForm
    model = models.MaquinariaAgricola
    list_url = "maquinaria_agricola_list"


class MaquinariaAgricolaDeleteView(views.DeleteView):
    model = models.MaquinariaAgricola
    list_url = "maquinaria_agricola_list"


class ZafraListView(views.ListView):
    model = models.Zafra
    table_class = tables.ZafraTable
    filterset_class = filters.ZafraFilter
    search_fields = ["descripcion", "item__descripcion"]
    update_url = "zafra_update"
    delete_url = "zafra_delete"
    create_url = "zafra_create"


class ZafraCreateView(views.CreateView):
    form_class = forms.ZafraForm
    model = models.Zafra
    list_url = "zafra_list"


class ZafraUpdateView(views.UpdateView):
    form_class = forms.ZafraForm
    model = models.Zafra
    list_url = "zafra_list"


class ZafraDeleteView(views.DeleteView):
    model = models.Zafra
    list_url = "zafra_list"


class LoteListView(views.ListView):
    model = models.Lote
    table_class = tables.LoteTable
    search_fields = ["descripcion", "item__descripcion"]
    update_url = "lote_update"
    delete_url = "lote_delete"
    create_url = "lote_create"


class LoteCreateView(views.CreateView):
    form_class = forms.LoteForm
    model = models.Lote
    list_url = "lote_list"


class LoteUpdateView(views.UpdateView):
    form_class = forms.LoteForm
    model = models.Lote
    list_url = "lote_list"


class LoteDeleteView(views.DeleteView):
    model = models.Lote
    list_url = "lote_list"


class PlanActividadZafraListView(views.ListView):
    model = models.PlanActividadZafra
    table_class = tables.PlanActividadZafraTable
    filterset_class = filters.PlanActividadZafraFilter
    search_fields = ["zafra__descripcion", "observacion"]
    update_url = "plan_actividad_zafra_update"
    create_url = "plan_actividad_zafra_create"
    delete_url = None


class PlanActividadZafraCreateView(views.CreateView):
    model = models.PlanActividadZafra
    form_class = forms.PlanActividadZafraForm
    inlines = [inlines.PlanActividadZafraDetalleInline]
    list_url = "plan_actividad_zafra_list"


class PlanActividadZafraUpdateView(views.UpdateView):
    model = models.PlanActividadZafra
    form_class = forms.PlanActividadZafraForm
    inlines = [inlines.PlanActividadZafraDetalleInline]
    list_url = "plan_actividad_zafra_list"


class ContratoListView(views.ListView):
    model = models.Contrato
    table_class = tables.ContratoTable
    search_fields = ["descripcion", "item__descripcion"]
    update_url = "contrato_update"
    delete_url = "contrato_delete"
    create_url = "contrato_create"


class ContratoCreateView(views.CreateView):
    form_class = forms.ContratoForm
    model = models.Contrato
    list_url = "contrato_list"


class ContratoDeleteView(views.DeleteView):
    model = models.Contrato
    list_url = "contrato_list"


class AcopioListView(views.ListView):
    model = models.Acopio
    table_class = tables.AcopioTable
    search_fields = ["zafra__descripcion", "comprobante", "deposito__descripcion"]
    update_url = "acopio_update"
    delete_url = "acopio_delete"
    create_url = "acopio_create"


class AcopioCreateView(views.CreateView):
    model = models.Acopio
    form_class = forms.AcopioForm
    inlines = [inlines.AcopioDetalleInline, inlines.AcopioCalificacionDetalleInline]
    list_url = "acopio_list"

    def run_form_extra_validation(self, form, inlines):
        acopio_detalle = inlines[0]
        total_peso = 0
        existe_registro = False
        peso_encabezado = (
            form.cleaned_data.get("peso_bruto")
            + form.cleaned_data.get("peso_bonificacion")
        ) - (
            form.cleaned_data.get("peso_tara") + form.cleaned_data.get("peso_descuento")
        )

        for f in acopio_detalle:
            total_peso = total_peso + f.cleaned_data.get("peso")
            existe_registro = True

        if existe_registro == False or total_peso == 0 or total_peso is None:
            form.add_error(None, "Registre al menos un detalle del acopio")

        if peso_encabezado != total_peso:
            form.add_error(
                "peso_bruto",
                "El neto (Peso Bruto + Peso Bonificacion ) - ( Peso Tara + Peso Descuento) no es igual a los detalles cargados",
            )


class AcopioUpdateView(views.UpdateView):
    model = models.Acopio
    form_class = forms.AcopioForm
    list_url = "acopio_list"
    inlines = [inlines.AcopioDetalleInline, inlines.AcopioCalificacionDetalleInline]


class AcopioAnnulledView(views.AnnulledView):
    model = models.Acopio
    list_url = "acopio_list"
    mensaje_anulacion = "El acopio ya fue anulado."


class ActividadAgricolaListView(views.ListView):
    model = models.ActividadAgricola
    table_class = tables.ActividadAgricolaTable
    search_fields = [
        "zafra__descripcion",
        "finca__descripcion",
        "lote__descripcion",
        "empleado__razon_social",
        "deposito__descripcion",
    ]
    update_url = None
    delete_url = "actividad_agricola_delete"
    create_url = "actividad_agricola_create"


class ActividadAgricolaCreateView(views.CreateView):
    model = models.ActividadAgricola
    form_class = forms.ActividadAgricolaForm
    inlines = [
        inlines.ActividadAgricolaMaquinariaDetalleInline,
        inlines.ActividadAgricolaItemDetalleInline,
    ]
    list_url = "actividad_agricola_list"

    def run_form_extra_validation(self, form, inlines):
        """ejecutar validaciones adicionales de formularios"""
        detalle_maquinaria = inlines[0]
        detalle_item = inlines[1]

        cantidad_ha_maquinaria = 0

        for f in detalle_maquinaria:
            cantidad_maquinaria = f.cleaned_data.get("ha_trabajada")
            if cantidad_maquinaria is None:
                cantidad_maquinaria = 0
            cantidad_ha_maquinaria += cantidad_maquinaria

        if (
            (cantidad_ha_maquinaria != form.cleaned_data.get("cantidad_trabajada"))
            and form.cleaned_data.get("es_servicio_contratado") == False
            and cantidad_ha_maquinaria > 0
        ):
            form.add_error(
                None,
                "La cantidad de HA trabajada debe ser igual a la cantidad de HA trabajada por las maquinarias",
            )


class ActividadAgricolaAnnulledView(views.AnnulledView):
    model = models.ActividadAgricola
    template_name = "inventory/anular.html"
    list_url = "actividad_agricola_list"
    mensaje_anulacion = "La Actividad Agrícola ya fue anulado."


class LiquidacionAgricolaListView(views.ListView):
    model = models.LiquidacionAgricola
    table_class = tables.LiquidacionAgricolaTable
    search_fields = ["proveedor__razon_social", "zafra__descripcion", "tipo"]
    update_url = None
    delete_url = None  #'actividad_agricola_delete'
    create_url = "liquidacion_agricola_selection"  #'actividad_agricola_create'


class LiquidacionAgricolaSelectionView(views.SelectionFormView):
    model = models.LiquidacionAgricola
    form_class = forms.LiquidacionAgricolaSelectionForm
    next_url = "liquidacion_agricola_create"
    back_url = "liquidacion_agricola_list"
    list_url = "liquidacion_agricola_list"
    selection_title = "Complete los filtros para continuar"


class LiquidacionAgricolaCreateView(views.CreateView):
    model = models.LiquidacionAgricola
    form_class = forms.LiquidacionAgricolaForm
    inlines = [inlines.LiquidacionAgricolaDetalleInline]
    list_url = "liquidacion_agricola_list"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.request.GET.get("zafra", None):
            form.fields["zafra"].initial = self.request.GET.get("zafra", None)
            form.fields["zafra"].widget.attrs.update(
                {"readonly": True, "style": "pointer-events:none;"}
            )
        if self.request.GET.get("proveedor", None):
            form.fields["proveedor"].initial = self.request.GET.get("proveedor", None)
            form.fields["proveedor"].widget.attrs.update(
                {"readonly": True, "style": "pointer-events:none;"}
            )
        if self.request.GET.get("tipo", None):
            form.fields["tipo"].initial = self.request.GET.get("tipo", None)
            form.fields["tipo"].widget.attrs.update(
                {"readonly": True, "style": "pointer-events:none;"}
            )
        if self.request.GET.get("precio_unitario", None):
            form.fields["precio_unitario"].initial = self.request.GET.get(
                "precio_unitario", None
            )
            form.fields["precio_unitario"].widget.attrs.update(
                {"readonly": True, "style": "pointer-events:none;"}
            )
        return form

    def get_inlines(self):
        inlines = super().get_inlines()
        zafra_select = self.request.GET.get("zafra", None)
        tipo_select = self.request.GET.get("tipo", None)
        precio = self.request.GET.get("precio_unitario", None)

        if tipo_select == "ACTIVIDADES AGRICOLAS":
            initial = [
                {
                    "precio": precio,
                    "secuencia_origen": x.pk,
                    "check": False,
                    "movimiento": x.tipoActividadAgricola.descripcion,
                    "finca": x.finca,
                    "lote": x.lote,
                    "cantidad": x.cantidad_trabajada,
                    "sub_total": round((float(x.cantidad_trabajada) * float(precio))),
                }
                for x in models.ActividadAgricola.objects.filter(
                    es_vigente=True, es_servicio_contratado=True
                )
                if not models.LiquidacionAgricolaDetalle.objects.filter(
                    liquidacion_agricola__es_vigente=True,
                    secuencia_origen=x.pk,
                    liquidacion_agricola__tipo="ACTIVIDADES AGRICOLAS",
                ).exists()
            ]
        else:
            initial = [
                {
                    "precio": precio,
                    "secuencia_origen": x.pk,
                    "check": False,
                    "movimiento": "Comp:"
                    + x.acopio.comprobante
                    + " Conductor "
                    + x.acopio.conductor.razon_social,
                    "finca": x.finca,
                    "lote": x.lote,
                    "cantidad": x.acopio.peso_bruto,
                    "sub_total": round((float(x.acopio.peso_bruto) * float(precio))),
                }
                for x in models.AcopioDetalle.objects.filter(
                    acopio__es_vigente=True, acopio__es_transportadora_propia=False
                )
                if not models.LiquidacionAgricolaDetalle.objects.filter(
                    liquidacion_agricola__es_vigente=True,
                    secuencia_origen=x.pk,
                    liquidacion_agricola__tipo="ACOPIOS",
                ).exists()
            ]
        inlines[0].initial = initial
        inlines[0].factory_kwargs["extra"] = len(initial)
        inlines[0].factory_kwargs["can_delete"] = False

        return inlines

    def run_form_extra_validation(self, form, inlines):
        """ejecutar validaciones adicionales de formularios"""
        detalle = inlines[0]
        existe_un_seleccionado = False

        for f in detalle:
            if f.cleaned_data.get("check"):
                existe_un_seleccionado = True

        if existe_un_seleccionado == False:
            form.add_error(None, "Seleccione al menos un detalle a liquidar")


class LiquidacionAgricolaAnnulledView(views.AnnulledView):
    model = models.LiquidacionAgricola
    list_url = "liquidacion_agricola_list"
    mensaje_anulacion = "La Liquidacion Agrícola ya fue anulado."


class CierreZafraListView(views.ListView):
    model = models.CierreZafra
    table_class = tables.CierreZafraTable
    search_fields = [
        "zafra__descripcion",
    ]
    update_url = None
    delete_url = "cierre_zafra_delete"
    create_url = "cierre_zafra_selection"


class CierreZafraDeleteView(views.DeleteView):
    model = models.CierreZafra
    list_url = "cierre_zafra_list"


class CierreZafraSelectionView(views.SelectionFormView):
    model = models.CierreZafra
    form_class = forms.CierreZafraSelectionForm
    list_url = "cierre_zafra_list"
    next_url = "cierre_zafra_create"
    back_url = "cierre_zafra_list"
    title = "Complete los filtros para continuar"
    params_name = "zafra"


class CierreZafraCreateView(views.CreateView):
    model = models.CierreZafra
    form_class = forms.CierreZafraForm
    inlines = [inlines.CierreZafraDetalleInline]
    list_url = "cierre_zafra_list"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.request.GET.get("zafra", None):
            form.fields["zafra"].initial = self.request.GET.get("zafra", None)
            form.fields["zafra"].widget.attrs.update(
                {"readonly": True, "style": "pointer-events:none;"}
            )
        return form

    def run_form_extra_validation(self, form, inlines):
        """ejecutar validaciones adicionales de formularios"""
        detalle = inlines[0]
        existe_finca_sin_plantacion = False
        existe_sin_costo = False
        existe_sin_acopio = False
        existe_sin_selecionar = False

        for f in detalle:
            if (
                f.cleaned_data.get("check") == False
                or f.cleaned_data.get("check") is None
            ):
                existe_sin_selecionar = True
            if (
                f.cleaned_data.get("ha_cultivada") == 0
                or f.cleaned_data.get("ha_cultivada") is None
            ):
                existe_finca_sin_plantacion = True
            if (
                f.cleaned_data.get("cantidad_acopio_neto") == 0
                or f.cleaned_data.get("cantidad_acopio_neto") is None
            ):
                existe_sin_acopio = True
            print(
                "ha_cultivada",
                f.cleaned_data.get("ha_cultivada"),
                "cantidad_acopio_neto",
                f.cleaned_data.get("cantidad_acopio_neto"),
                "costo_total",
                f.cleaned_data.get("costo_total"),
            )
            if (
                f.cleaned_data.get("costo_total") == 0
                or f.cleaned_data.get("costo_total") is None
            ):
                existe_sin_costo = True

        if existe_sin_selecionar == True:
            form.add_error(None, "Confirme todos los detalles para guardar")

        if existe_sin_selecionar == False:
            if existe_finca_sin_plantacion == True:
                form.add_error(
                    None,
                    "Algun/as Finca/as no tienen una actividad de plantación registrada. Proceda a registrar para poder cerrar la zafra",
                )
            if existe_sin_acopio == True:
                form.add_error(
                    None,
                    "Algun/as Finca/as no tienen registrado Acopio/s. Proceda a registrar para poder cerrar la zafra",
                )
            if existe_sin_costo == True:
                form.add_error(
                    None,
                    "Algun/as Finca/as no tienen registrados Gastos. Proceda a registrar para poder cerrar la zafra",
                )

    def get_inlines(self):
        initial = []
        zafra_digitada = self.request.GET.get("zafra", None)
        for finca_det in models.Finca.objects.all():
            ha_cultivada_v = models.ActividadAgricola.objects.filter(
                es_vigente=True,
                tipo_actividad_agricola__es_siembra=True,
                zafra=zafra_digitada,
                finca=finca_det,
            ).aggregate(Sum("cantidad_trabajada"))
            cantidad_acopio = models.AcopioDetalle.objects.filter(
                acopio__es_vigente=True, acopio__zafra=zafra_digitada, finca=finca_det
            ).aggregate(Sum("peso"))
            costo_item = models.ActividadAgricolaItemDetalle.objects.annotate(
                i_sum=Sum(F("costo") * F("cantidad"))
            ).filter(
                actividad_agricola__es_vigente=True,
                actividad_agricola__zafra=zafra_digitada,
                actividad_agricola__finca=finca_det,
            )
            costo_maquinaria = (
                models.ActividadAgricolaMaquinariaDetalle.objects.annotate(
                    i_sum=Sum(F("ha_trabajada") * F("ha_trabajada"))
                ).filter(
                    actividad_agricola__es_vigente=True,
                    actividad_agricola__zafra=zafra_digitada,
                    actividad_agricola__finca=finca_det,
                )
            )
            costo_liquidacion = models.LiquidacionAgricolaDetalle.objects.annotate(
                i_sum=Sum(F("cantidad") * F("liquidacion_agricola__precioUnitario"))
            ).filter(
                liquidacion_agricola__es_vigente=True,
                liquidacion_agricola__zafra=zafra_digitada,
                finca=finca_det,
            )
            costo_item_total = 0
            costo_maquinaria_total = 0
            costo_liquidacion_total = 0
            costo_total = 0
            hectareas_cultivadas = ha_cultivada_v.get("cantidad_trabajada__sum")
            acopios = cantidad_acopio.get("peso__sum")
            rendimiento_kg = 0
            costo_ha = 0
            costo_unit = 0

            for x in costo_item:
                costo_item_total += x.i_sum

            for x in costo_maquinaria:
                costo_maquinaria_total += x.i_sum

            for x in costo_liquidacion:
                costo_liquidacion_total += x.i_sum

            if hectareas_cultivadas is None:
                hectareas_cultivadas = 0

            if acopios is None:
                acopios = 0

            costo_total = (
                costo_item_total + costo_maquinaria_total + costo_liquidacion_total
            )

            if hectareas_cultivadas != 0 and acopios != 0:

                rendimiento_kg = round(acopios / hectareas_cultivadas)

                costo_ha = round(costo_total / hectareas_cultivadas)

                costo_unit = round(costo_total / acopios)

            if costo_total != 0 or acopios != 0 or hectareas_cultivadas != 0:
                initial += [
                    {
                        "check": False,
                        "finca": finca_det,
                        "ha_cultivada": hectareas_cultivadas,
                        "cantidad_acopio_neto": round(acopios),
                        "rendimiento": round(rendimiento_kg),
                        "costo_total": round(costo_total),
                        "costo_ha": round(costo_ha),
                        "costo_unit": round(costo_unit),
                    }
                ]

        detalle = self.inlines[0]
        detalle.initial = initial
        detalle.factory_kwargs["extra"] = len(initial)
        detalle.factory_kwargs["can_delete"] = False
        return self.inlines
