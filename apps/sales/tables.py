from apps.sales.models import AperturaCaja
from core.tables import AccionTable
from core.tables.columns import BooleanColumn, TotalNumericColumn

class AperturaCajaTable(AccionTable):
    total = TotalNumericColumn(verbose_name = 'Total')
    esta_cerrado = BooleanColumn()
    class Meta:
        model = AperturaCaja
        fields = ("empleado","fecha_hora_registro","fecha_hora_cierre","monto_inicio","esta_cerrado")