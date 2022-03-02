import django_tables2 as tables

class BaseTable(tables.Table):
    def __init__(self, *args, **kwargs):
        kwargs['empty_text']  =  "Sin resultados." 
        super().__init__(*args, **kwargs)
        self.template_name = "django_tables2/bootstrap4.html"

class SingleTable(BaseTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

class EditableTable(BaseTable):
    def __init__(self, *args, **kwargs):
        kwargs['extra_columns'] = [
            (
                'editar', 
                tables.TemplateColumn(
                    template_name="includes/edit_button.html", 
                    verbose_name="Editar", 
                    orderable=False,
                    attrs={
                        'th':{
                            'class':'col-sm-1 text-center',
                        },
                        'td':{
                            'class':'col-sm-1 text-center',
                        }
                    }
                )
            ),
            (
                'eliminar', 
                tables.TemplateColumn(
                    template_name="includes/delete_button.html", 
                    verbose_name="Eliminar", 
                    orderable=False,
                    attrs={
                        'th':{
                            'class':'col-sm-1 text-center',
                        },
                        'td':{
                            'class':'col-sm-1 text-center',
                        }
                    }
                )
            )
        ]
        super().__init__(*args, **kwargs)