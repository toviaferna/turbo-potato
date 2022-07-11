from apps.sales.models import AperturaCaja
from core.tables import AccionTable
from core.tables.columns import (BooleanColumn, NumericColumn,
                                 TotalNumericColumn)


class AperturaCajaTable(AccionTable):
    monto_inicio = NumericColumn()
    esta_cerrado = BooleanColumn()
    class Meta:
        model = AperturaCaja
        fields = ("empleado","fecha_hora_registro","fecha_hora_cierre","monto_inicio","esta_cerrado")
