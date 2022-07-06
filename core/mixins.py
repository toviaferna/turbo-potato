from django.core.exceptions import FieldDoesNotExist
from django.db.models import Q
from django.urls import reverse_lazy


class SearchViewMixin: 
    search_fields = None

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_fields:
            or_condition = Q()
            value = self.get_search_query()
            if value:
                for field in self.search_fields:
                    or_condition.add(Q(**{f"{field}__icontains": value}), Q.OR)
                queryset = queryset.filter(or_condition)

        return queryset

    def get_search_query(self):
        return self.request.GET.get('q', None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.get_search_query()
        context['search_placeholder'] = self.get_search_placeholder()
        #agregar bandera para ocultara en generic list
        context['search'] = True
        return context
    

    def _get_model_name_by_lookup(self, lookup):
        model = self.model
        for name in lookup.split('__'):
            try:
                field = model._meta.get_field(name)
            except FieldDoesNotExist:
                # name is probably a lookup or transform such as __contains
                break
            if hasattr(field, 'related_model'):
                # field is a relation
                if field.related_model:
                    model = field.related_model
                
            else:
                # field is not a relation, any name that follows is
                # probably a lookup or transform
                break
        return model

    def get_search_placeholder(self):
        placeholder = ""
        labels=[]
        model = self.model
        for field in self.search_fields:
            if len(field.split('__')) == 1: 
                labels.append(model._meta.get_field(field).verbose_name)
            else:
                related = self._get_model_name_by_lookup(field)
                model_name = related._meta.verbose_name
                try:
                    field_name = field.split('__')[-1:][0]
                    label = related._meta.get_field(field_name).verbose_name
                    labels.append(f"{model_name}: {label}")
                except FieldDoesNotExist:
                    pass
        if labels:
            placeholder = ", ".join(map(str.capitalize, map(str, labels)))
        return placeholder

class SelectionMixin:
    selection_title = None
    next_url = None
    back_url = None
    template_name = 'generic/selection.html'
    params_name = 'selection-pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selection_title'] = self.selection_title
        context['next_url'] = None if not self.next_url else self.next_url
        context['back_url'] = None if not self.back_url else self.back_url
        context['params_name'] = self.params_name
        return context
