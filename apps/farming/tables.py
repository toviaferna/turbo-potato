from core.tables import AccionTable
from core.tables.columns import NumericColumn, TotalNumericColumn
from django_tables2 import Column

from .models import (Acopio, ActividadAgricola, CalificacionAgricola,
                     CierreZafra, Contrato, Finca, LiquidacionAgricola, Lote,
                     MaquinariaAgricola, TipoActividadAgricola,
                     TipoMaquinariaAgricola, Zafra)


class FincaTable(AccionTable):

    class Meta:
        model = Finca
        fields = ("descripcion","dimension_ha","ubicacion")

class CalificacionAgricolaTable(AccionTable):
    class Meta:
        model = CalificacionAgricola
        fields = ("descripcion",)

class TipoMaquinariaAgricolaTable(AccionTable):
    class Meta:
        model = TipoMaquinariaAgricola
        fields = ("descripcion",)

class MaquinariaAgricolaTable(AccionTable):
    precio = NumericColumn()
    class Meta:
        model = MaquinariaAgricola
        fields = ("descripcion","tipo_maquinaria_agricola", "es_implemento","admite_implemento","precio")

class TipoActividadAgricolaTable(AccionTable):
    class Meta:
        model = TipoActividadAgricola
        fields = ("descripcion","es_cosecha","es_siembra","es_resiembra")

class ZafraTable(AccionTable):
    class Meta:
        model = Zafra
        fields = ("descripcion","item", "es_zafrinha","anho","esta_cerrado")

class LoteTable(AccionTable):
    class Meta:
        model = Lote
        fields = ("descripcion","zafra", "finca")

class PlanActividadZafraTable(AccionTable):
    total = TotalNumericColumn(verbose_name = 'Total')
    class Meta:
        model = Lote
        fields = ("fecha","zafra","observacion","total")


class ContratoTable(AccionTable):
    costo_pactado = NumericColumn()
    class Meta:
        model = Contrato
        fields = ("fecha","zafra","persona","costo_pactado","descripcion")

class AcopioTable(AccionTable):

    peso_bruto = NumericColumn()
    peso_tara = NumericColumn()
    peso_descuento =  NumericColumn()
    total = NumericColumn()

    class Meta:
        model = Acopio
        fields = ("fecha","comprobante","zafra","deposito","peso_bruto","peso_tara","peso_descuento","total","es_vigente")
        row_attrs = {
            "es-vigente": lambda record: record.es_vigente
        }
        order_by = "-fecha"

class ActividadAgricolaTable(AccionTable):
    cantidad_trabajada = NumericColumn()
    total = NumericColumn()
    class Meta:
        model = ActividadAgricola
        fields = ("fecha_documento","tipo_actividad_agricola","zafra","finca","lote","cantidad_trabajada","es_servicio_contratado","total","es_vigente")
        row_attrs = {
            "es-vigente": lambda record: record.es_vigente
        }
        order_by = "-fecha_documento"

class LiquidacionAgricolaTable(AccionTable):
    total = NumericColumn()
    class Meta:
        model = LiquidacionAgricola
        fields = ("fecha_documento","tipo","zafra","proveedor","total","es_vigente")
        row_attrs = {
            "es-vigente": lambda record: record.es_vigente
        }
        order_by = "-fecha_documento"

class CierreZafraTable(AccionTable):
    total_acopiado = NumericColumn(verbose_name= 'KG Acopiado')
    total_cultivado = NumericColumn(verbose_name= 'HA Cultivada')
    total_costo_unit = NumericColumn(verbose_name= 'Costo Unit',)
    total_costo_ha = NumericColumn(verbose_name= 'Costo HA')
    total_costo = NumericColumn(verbose_name= 'Costo')
    class Meta:
        model = CierreZafra
        fields = ("fecha","zafra","total_cultivado","total_acopiado","total_costo","total_costo_ha","total_costo_unitario")
        order_by = "-fecha"
