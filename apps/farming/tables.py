from core.tables import AccionTable
from core.tables.columns import NumericColumn, TotalNumericColumn

from .models import (CalificacionAgricola, Contrato, Finca, Lote,
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
