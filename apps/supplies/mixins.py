class FormsetInlinesMetaMixin(object):
    _formset_inlines_meta = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.build_formset_inlines_meta()

    def build_formset_inlines_meta(self):
        if not hasattr(self, 'inlines'):
            return None

        for i, formset_class in enumerate(self.inlines):
            self._formset_inlines_meta[formset_class.__name__] = { 'index': i }

    def get_formset_inlines_meta(self):
        return self._formset_inlines_meta

    def get_context_data(self, **kwargs):
        """
            get and update context data
        """
        context = super().get_context_data(**kwargs)
        context['formset_inlines_meta'] = self.get_formset_inlines_meta()
        return context