from django_tables2 import tables

class BaseTable(tables.Table):
    def __init__(self, *args, **kwargs):
        kwargs['empty_text']  =  "Sin resultados." 
        super().__init__(*args, **kwargs)
        self.template_name = "django_tables2/bootstrap4.html"

class EditableTable(BaseTable):
    def __init__(self, *args, **kwargs):
        kwargs['extra_columns'] = [('editar', tables.TemplateColumn(template_name="includes/edit_button.html", verbose_name="Editar", orderable=False))]
        super().__init__(*args, **kwargs)