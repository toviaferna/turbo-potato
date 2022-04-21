from django_tables2.export import views

class ExportMixin(views.ExportMixin):
    export_page_orientation = "portrait"
    
    def create_export(self, export_format):
        exporter = self.export_class(
            export_format=export_format,
            table=self.get_table(**self.get_table_kwargs()),
            exclude_columns=self.exclude_columns,
            page_orientation=self.export_page_orientation,
            dataset_kwargs=self.get_dataset_kwargs(),
        )

        return exporter.response(filename=self.get_export_filename(export_format))