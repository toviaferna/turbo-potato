from apps.inventory import models
from dal import autocomplete
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Q
from django.utils.html import format_html


class ProductoAutocomplete(autocomplete.Select2QuerySetView):
    
    def get_result_label(self, result):
        return super().get_result_label(result)

    def get_selected_result_label(self, result):
        return super().get_selected_result_label(result)
    
    def get_queryset(self):

        fields = ["codigo_barra", "descripcion", "marca__descripcion", "categoria__descripcion"]
        if not self.request.user.is_authenticated:
            return models.Item.objects.none()
        qs = models.Item.objects.all().filter(es_activo=True)
        or_condition = Q()
        
        if self.q:
            for field in fields:
                or_condition.add(Q(**{f"{field}__icontains": self.q}), Q.OR)
            qs = qs.filter(or_condition, )
        
        return qs

class ProductoNormalAutocomplete(autocomplete.Select2QuerySetView):
    
    def get_result_label(self, result):
        return super().get_result_label(result)

    def get_selected_result_label(self, result):
        return super().get_selected_result_label(result)
    
    def get_queryset(self):

        fields = ["codigo_barra", "descripcion", "marca__descripcion", "categoria__descripcion"]
        if not self.request.user.is_authenticated:
            return models.Item.objects.none()
        qs = models.Item.objects.all().filter(es_activo=True, tipo_item__pk=2)
        or_condition = Q()
        
        if self.q:
            for field in fields:
                or_condition.add(Q(**{f"{field}__icontains": self.q}), Q.OR)
            qs = qs.filter(or_condition, )
        
        return qs

class ProductoAgricolaAutocomplete(autocomplete.Select2QuerySetView):
    
    def get_result_label(self, result):
        return super().get_result_label(result)

    def get_selected_result_label(self, result):
        return super().get_selected_result_label(result)
    
    def get_queryset(self):

        fields = ["codigo_barra", "descripcion", "marca__descripcion", "categoria__descripcion"]
        if not self.request.user.is_authenticated:
            return models.Item.objects.none()
        qs = models.Item.objects.all().filter(es_activo=True, tipo_item__pk=1)
        or_condition = Q()
        
        if self.q:
            for field in fields:
                or_condition.add(Q(**{f"{field}__icontains": self.q}), Q.OR)
            qs = qs.filter(or_condition, )
        
        return qs
