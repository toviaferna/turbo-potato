from apps.finance import models
from dal import autocomplete
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Q
from django.utils.html import format_html


class PersonaAutocomplete(autocomplete.Select2QuerySetView):
    
    es_proveedor = None
    es_empleado = None
    es_cliente = None

    def get_result_label(self, result):
        return super().get_result_label(result)

    def get_selected_result_label(self, result):
        return super().get_selected_result_label(result)
    
    def get_queryset(self):

        fields = ["razon_social", "documento"]
       
        if not self.request.user.is_authenticated:
            return models.Persona.objects.none()
        if self.es_proveedor:
            qs = models.Persona.objects.all().filter(es_proveedor=True)
        elif self.es_cliente:
            qs = models.Persona.objects.all().filter(es_cliente=True)
        elif self.es_empleado:
            qs = models.Persona.objects.all().filter(es_empleado=True)
        else:
            qs = models.Persona.objects.all()
        or_condition = Q()
        
        if self.q:
            for field in fields:
                or_condition.add(Q(**{f"{field}__icontains": self.q}), Q.OR)
            qs = qs.filter(or_condition, )
        
        return qs
