from django.urls.base import reverse
from django.utils.html import format_html

from apps.farming import models
from core.tables import AccionTable, DetailTable
from core.tables.columns import NumericColumn, TotalNumericColumn


class FincaTable(AccionTable):
    class Meta:
        model = models.Finca
        fields = ("descripcion", "dimension_ha", "ubicacion")


class CalificacionAgricolaTable(AccionTable):
    class Meta:
        model = models.CalificacionAgricola
        fields = ("descripcion",)


class TipoMaquinariaAgricolaTable(AccionTable):
    class Meta:
        model = models.TipoMaquinariaAgricola
        fields = ("descripcion",)


class MaquinariaAgricolaTable(AccionTable):
    precio = NumericColumn()

    class Meta:
        model = models.MaquinariaAgricola
        fields = (
            "descripcion",
            "tipo_maquinaria_agricola",
            "es_implemento",
            "admite_implemento",
            "precio",
        )


class TipoActividadAgricolaTable(AccionTable):
    class Meta:
        model = models.TipoActividadAgricola
        fields = ("descripcion", "es_cosecha", "es_siembra", "es_resiembra")


class ZafraTable(AccionTable):
    class Meta:
        model = models.Zafra
        fields = ("descripcion", "item", "es_zafrinha", "anho", "esta_cerrado")


class LoteTable(AccionTable):
    class Meta:
        model = models.Lote
        fields = ("descripcion", "zafra", "finca")


class PlanActividadZafraTable(AccionTable):
    total = NumericColumn(verbose_name="Total")

    class Meta:
        model = models.Lote
        fields = ("fecha", "zafra", "observacion", "total")


class ContratoTable(AccionTable):
    costo_pactado = NumericColumn()

    class Meta:
        model = models.Contrato
        fields = ("fecha", "zafra", "persona", "costo_pactado", "descripcion")


class AcopioTable(AccionTable):

    peso_bruto = NumericColumn()
    peso_tara = NumericColumn()
    peso_descuento = NumericColumn()
    total = NumericColumn()

    class Meta:
        model = models.Acopio
        fields = (
            "fecha",
            "comprobante",
            "zafra",
            "deposito",
            "peso_bruto",
            "peso_tara",
            "peso_descuento",
            "total",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha"


class ActividadAgricolaTable(AccionTable):
    cantidad_trabajada = NumericColumn()
    total = NumericColumn()

    def render_tipo_actividad_agricola(self, value, record):
        return format_html(
            '<a href="{}">{}</a>',
            reverse("actividad_agricola_detail", kwargs={"pk": record.pk}),
            value,
        )

    class Meta:
        model = models.ActividadAgricola
        fields = (
            "fecha_documento",
            "tipo_actividad_agricola",
            "zafra",
            "finca",
            "lote",
            "cantidad_trabajada",
            "es_servicio_contratado",
            "total",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"

class ActividadAgricolaMaquinariaDetalleTable(DetailTable):
    ha_trabajada = NumericColumn()
    precio = NumericColumn()
    total = NumericColumn()
    class Meta:
        model = models.ActividadAgricolaMaquinariaDetalle
        fields = (
            "maquinaria__pk",
            "maquinaria__descripcion",
            "ha_trabajada",
            "precio",
            "total"
        )

class ActividadAgricolaItemDetalleTable(DetailTable):
    costo = NumericColumn()
    cantidad = NumericColumn()
    porcentaje_impuesto = NumericColumn()
    dosis = NumericColumn()
    class Meta:
        model = models.ActividadAgricolaItemDetalle
        fields = (
            "item__pk",
            "item__descripcion",
            "deposito__pk",
            "deposito__descripcion",
            "costo",
            "cantidad",
            "porcentaje_impuesto",
            "dosis",
        )

class LiquidacionAgricolaTable(AccionTable):
    total = NumericColumn()

    class Meta:
        model = models.LiquidacionAgricola
        fields = (
            "fecha_documento",
            "tipo",
            "zafra",
            "proveedor",
            "total",
            "es_vigente",
        )
        row_attrs = {"es-vigente": lambda record: record.es_vigente}
        order_by = "-fecha_documento"


class CierreZafraTable(AccionTable):
    total_acopiado = NumericColumn(verbose_name="KG Acopiado")
    total_cultivado = NumericColumn(verbose_name="HA Cultivada")
    total_costo_unitario = NumericColumn(
        verbose_name="Costo Unit",
    )
    total_costo_ha = NumericColumn(verbose_name="Costo HA")
    total_costo = NumericColumn(verbose_name="Costo")

    class Meta:
        model = models.CierreZafra
        fields = (
            "fecha",
            "zafra",
            "total_cultivado",
            "total_acopiado",
            "total_costo",
            "total_costo_ha",
            "total_costo_unitario",
        )
        order_by = "-fecha"
