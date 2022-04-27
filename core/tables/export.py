from io import BytesIO
from re import S
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

    def __init__(self, export_format, table, exclude_columns=None,page_orientation="portrait", dataset_kwargs=None):
        self.page_orientation = page_orientation
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
            'table_headers': self.dataset.headers, 
            'table_data': self.dataset._data, 
            'title': self.dataset.title,
            'today': timezone.now(),
            'orientation': self.page_orientation
        })
        return html

    def response(self, filename=None):
        filename = f"{self.dataset.title.upper()}_{timezone.now().strftime('%d%m%Y_%H%M%S')}.{self.format}".replace(" ","_")
        return super().response(filename)
    

    def export(self):
        if self.format == self.PDF:
            response = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(self.get_dataset_as_html().encode("UTF-8")), response)
            data = response.getvalue()
        elif self.format == self.HTML:
            return self.get_dataset_as_html().encode("UTF-8")
        else:
            data = self.dataset.export(self.format)
        return data
