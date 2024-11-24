from dal import autocomplete
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Q
from django.utils.html import format_html

from apps.farming import models


class MaquinariaAutocomplete(autocomplete.Select2QuerySetView): 
    tipo_item=None
    def get_result_label(self, result):

        return format_html(
            f"""
                <div class="container row" data-precio-ha={result.precio} >
                    <div class="col">{result.descripcion}</div>
                </div>
            """
        )

    def  get_selected_result_label(self, result):
        return result.descripcion
    
    def get_queryset(self):

        fields = ["descripcion", "tipo_maquinaria_agricola__descripcion"]
        
        if not self.request.user.is_authenticated:
            return models.MaquinariaAgricola.objects.none()
        
        qs = models.MaquinariaAgricola.objects.all()

        or_condition = Q()
        
        if self.q:
            for field in fields:
                or_condition.add(Q(**{f"{field}__icontains": self.q}), Q.OR)
            qs = qs.filter(or_condition, )
        
        return qs