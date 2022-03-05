from django_tables2.export import views
from core.tables.export import TableExport
class ExportMixin(views.ExportMixin):
    export_class = TableExport