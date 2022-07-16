from apps.farming import forms, models
from core.widgets import DateInput, ItemCustomSelect, MaquinariaCustomSelect
from django.forms import widgets
from extra_views import InlineFormSetFactory


class PlanActividadZafraDetalleInline(InlineFormSetFactory):
    model = models.PlanActividadZafraDetalle
    form_class = forms.PlanActividadZafraDetalleForm
    factory_kwargs = {
        "extra": 1,
        "widgets": {
            "fecha_actividad": DateInput(
                attrs={"wrapper_class": "col-sm-1", "type": "date"}
            ),
            "finca": widgets.Select(
                attrs={
                    "wrapper_class": "col-sm-2",
                }
            ),
            "tipo_actividad_agricola": widgets.Select(
                attrs={
                    "wrapper_class": "col-sm-2",
                }
            ),
            "costo": widgets.NumberInput(
                attrs={
                    "wrapper_class": "col-sm-2",
                }
            ),
        },
    }
    fields = [
        "fecha_actividad",
        "finca",
        "tipo_actividad_agricola",
        "descripcion",
        "costo",
    ]


class AcopioDetalleInline(InlineFormSetFactory):
    model = models.AcopioDetalle
    form_class = forms.AcopioDetalleForm
    factory_kwargs = {
        "extra": 1,
        "widgets": {
            "finca": widgets.Select(
                attrs={
                    "wrapper_class": "col-sm-5",
                }
            ),
            "lote": widgets.Select(
                attrs={
                    "wrapper_class": "col-sm-4",
                }
            ),
            #'peso':DecimalMaskInput()
        },
    }
    fields = ["acopio", "finca", "lote", "peso"]


class AcopioCalificacionDetalleInline(InlineFormSetFactory):
    model = models.AcopioCalificacion
    form_class = forms.AcopioCalificacionForm
    factory_kwargs = {
        "extra": 1,
        "widgets": {
            "calificacion_agricola": widgets.Select(
                attrs={
                    "wrapper_class": "col-sm-5",
                }
            ),
        },
    }
    fields = ["acopio", "calificacion_agricola", "grado", "porcentaje", "peso"]


class ActividadAgricolaMaquinariaDetalleInline(InlineFormSetFactory):
    model = models.ActividadAgricolaMaquinariaDetalle
    form_class = forms.ActividadAgricolaMaquinariaDetalleForm
    factory_kwargs = {
        "extra": 1,
        "widgets": {
            "maquinaria": MaquinariaCustomSelect(
                attrs={
                    "wrapper_class": "col-sm-4",
                    "data-maquinaria-select": True,
                }
            ),
            "precio": widgets.NumberInput(
                attrs={
                    "class": "text-right precio-ha",
                }
            ),
        },
    }
    fields = ["maquinaria", "ha_trabajada", "precio", "subtotal_maquinaria"]


class ActividadAgricolaItemDetalleInline(InlineFormSetFactory):
    model = models.ActividadAgricolaItemDetalle
    form_class = forms.ActividadAgricolaItemDetalleForm
    factory_kwargs = {
        "extra": 1,
        "widgets": {
            "item": ItemCustomSelect(
                attrs={
                    "wrapper_class": "col-sm-2",
                    "data-item-select": True,
                }
            ),
            "porcentaje_impuesto": widgets.NumberInput(
                attrs={
                    "class": "text-right item-porcentaje-impuesto",
                }
            ),
            "costo": widgets.NumberInput(
                attrs={
                    "class": "text-right item-costo",
                }
            ),
            "cantidad": widgets.NumberInput(
                attrs={
                    "wrapper_class": "col-sm-1",
                }
            ),
        },
    }
    fields = [
        "item",
        "deposito",
        "dosis",
        "costo",
        "cantidad",
        "porcentaje_impuesto",
        "subtotal_item",
    ]


class LiquidacionAgricolaDetalleInline(InlineFormSetFactory):
    model = models.LiquidacionAgricolaDetalle
    form_class = forms.LiquidacionAgricolaDetalleForm
    factory_kwargs = {"extra": 1}
    fields = [
        "secuencia_origen",
        "check",
        "movimiento",
        "finca",
        "lote",
        "cantidad",
        "sub_total",
    ]


class CierreZafraDetalleInline(InlineFormSetFactory):
    model = models.CierreZafraDetalle
    form_class = forms.CierreZafraDetalleForm
    factory_kwargs = {"extra": 1}
    fields = [
        "check",
        "finca",
        "ha_cultivada",
        "cantidad_acopio_neto",
        "rendimiento",
        "costo_total",
        "costo_ha",
        "costo_unitario",
    ]
