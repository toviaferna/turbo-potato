import django_tables2 as tables

class BaseTable(tables.Table):
    def __init__(self, *args, **kwargs):
        kwargs['empty_text']  =  "Sin resultados." 
        super().__init__(*args, **kwargs)
        self.template_name = "django_tables2/bootstrap4.html"

class SingleTable(BaseTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

class AccionTable(BaseTable):
    def __init__(self, *args, **kwargs):
        kwargs['extra_columns'] = [
            (
                'acciones', 
                tables.TemplateColumn(
                    template_name="includes/accion_button.html", 
                    verbose_name="Acciones", 
                    orderable=False,
                    attrs={
                        'th':{
                            'class':'col-sm-2 text-center',
                        },
                        'td':{
                            'class':'col-sm-2 text-center',
                        },
                        'tr':{
                            'prueba':True,
                        }
                    },
                    exclude_from_export=True
                )
            ),
        ]
        super().__init__(*args, **kwargs)
