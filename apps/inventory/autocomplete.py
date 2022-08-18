from apps.inventory import models
from dal import autocomplete
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Q
from django.utils.html import format_html


class ProductoAutocomplete(autocomplete.Select2QuerySetView):
    tipo_item=None
    def get_result_label(self, result):

        return format_html(
            f"""
                <div class="container row" data-precio={result.precio} data-costo={result.costo} data-ultimo-costo={result.ultimo_costo}  data-tipo-impuesto-id={result.tipo_impuesto.id} data-tipo-impuesto-descripcion={result.tipo_impuesto.descripcion} data-tipo-impuesto-porcentaje={result.tipo_impuesto.porcentaje} data-tipo-impuesto-iva={result.tipo_impuesto.es_iva}>
                    <div class="col">{result.descripcion}</div>
                     <!--<div class="col text-right">
                         <span class="badge badge-secondary text-right">{intcomma(result.precio)}</span>
                     </div>-->
                </div>
            """
        )

    def  get_selected_result_label(self, result):
        return result.descripcion
    
    def get_queryset(self):

        print(self.tipo_item)

        fields = ["codigo_barra", "descripcion", "marca__descripcion", "categoria__descripcion"]
        if not self.request.user.is_authenticated:
            return models.Item.objects.none()
        qs = models.Item.objects.all().filter(es_activo=True)
        if self.tipo_item:
            print("HEREEE")
            qs = models.Item.objects.all().filter(es_activo=True, tipo_item__pk=self.tipo_item)
        or_condition = Q()
        
        if self.q:
            for field in fields:
                or_condition.add(Q(**{f"{field}__icontains": self.q}), Q.OR)
            qs = qs.filter(or_condition, )
        
        return qs

