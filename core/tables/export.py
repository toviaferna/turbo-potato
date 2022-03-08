from io import BytesIO
from django_tables2.export import export
from django.utils import timezone
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
import uuid
class TableExport(export.TableExport):
    PDF = "pdf"
    CSV = "csv"
    HTML = "html"
    JSON = "json"
    LATEX = "latex"
    ODS = "ods"
    TSV = "tsv"
    XLS = "xls"
    XLSX = "xlsx"
    YAML = "yaml"

    FORMATS = {
        PDF: "application/pdf",
        CSV: "text/csv; charset=utf-8",
        HTML: "text/html; charset=utf-8",
        JSON: "application/json",
        LATEX: "text/plain",
        ODS: "application/vnd.oasis.opendocument.spreadsheet",
        TSV: "text/tsv; charset=utf-8",
        XLS: "application/vnd.ms-excel",
        XLSX: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        YAML: "text/yaml; charset=utf-8"
    }  

    def __init__(self, export_format, table, exclude_columns=None, dataset_kwargs=None):
        super().__init__(export_format, table, exclude_columns, dataset_kwargs)

    @classmethod
    def is_valid_format(self, export_format):
        """
        Returns true if `export_format` is one of the supported export formats
        """
        return export_format is not None and export_format in TableExport.FORMATS.keys()

    def get_dataset_as_html(self):
        template = get_template('django_tables2/export_pdf.html')
        html = template.render({
            'table': self.dataset.export("html"), 
            'title': self.dataset.title,
            'today': timezone.now()
        })
        return html

    def export(self):
        if self.format == self.PDF:
            response = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(self.get_dataset_as_html().encode("UTF-8")), response)
            data = response.getvalue()
        elif self.format == self.HTML:
            return self.get_dataset_as_html()
        else:
            data = self.dataset.export(self.format)
        return data
