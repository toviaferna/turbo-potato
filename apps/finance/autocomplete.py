from apps.finance import models
from dal import autocomplete
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Q
from django.utils.html import format_html


class ProveedorAutocomplete(autocomplete.Select2QuerySetView):
    
    def get_result_label(self, result):
        return super().get_result_label(result)

    def get_selected_result_label(self, result):
        return super().get_selected_result_label(result)
    
    def get_queryset(self):

        fields = ["razon_social", "documento"]
        if not self.request.user.is_authenticated:
            return models.Persona.objects.none()
        qs = models.Persona.objects.all().filter(es_proveedor=True)
        or_condition = Q()
        
        if self.q:
            for field in fields:
                or_condition.add(Q(**{f"{field}__icontains": self.q}), Q.OR)
            qs = qs.filter(or_condition, )
        
        return qs

class ClienteAutocomplete(autocomplete.Select2QuerySetView):
    
    def get_result_label(self, result):
        return super().get_result_label(result)

    def get_selected_result_label(self, result):
        return super().get_selected_result_label(result)
    
    def get_queryset(self):

        fields = ["razon_social", "documento"]
        if not self.request.user.is_authenticated:
            return models.Persona.objects.none()
        qs = models.Persona.objects.all().filter(es_cliente=True)
        or_condition = Q()
        
        if self.q:
            for field in fields:
                or_condition.add(Q(**{f"{field}__icontains": self.q}), Q.OR)
            qs = qs.filter(or_condition, )
        
        return qs

class EmpleadoAutocomplete(autocomplete.Select2QuerySetView):
    
    def get_result_label(self, result):
        return super().get_result_label(result)

    def get_selected_result_label(self, result):
        return super().get_selected_result_label(result)
    
    def get_queryset(self):

        fields = ["razon_social", "documento"]
        if not self.request.user.is_authenticated:
            return models.Persona.objects.none()
        qs = models.Persona.objects.all().filter(es_empleado=True)
        or_condition = Q()
        
        if self.q:
            for field in fields:
                or_condition.add(Q(**{f"{field}__icontains": self.q}), Q.OR)
            qs = qs.filter(or_condition, )
        
        return qs
