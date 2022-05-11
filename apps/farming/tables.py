from .models import CalificacionAgricola, Finca, MaquinariaAgricola, TipoActividadAgricola, TipoMaquinariaAgricola
from core.tables import AccionTable
from core.tables.columns import NumericColumn

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

