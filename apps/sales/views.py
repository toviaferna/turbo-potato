import datetime

from apps.sales.filters import AperturaCajaFilter
from apps.sales.forms import AperturaCajaCreateForm
from apps.sales.models import AperturaCaja
from apps.sales.tables import AperturaCajaTable
from core.views import CreateView, DeleteView, ListView
from django.db import transaction
from django.http import HttpResponseRedirect


# Create your views here.
class AperturaCajaListView(ListView):
    model = AperturaCaja
    table_class = AperturaCajaTable
    filterset_class = AperturaCajaFilter
    search_fields = ['empleado__razon_social','observacion']
    update_url = None
    create_url = "apertura_caja_create"#'apertura_caja_create'
    delete_url = "apertura_caja_delete"#'apertura_caja_delete'

class AperturaCajaCreateView(CreateView):
    form_class = AperturaCajaCreateForm
    model = AperturaCaja
    list_url = "apertura_caja_list"

class AperturaCajaDeleteView(DeleteView):
    model = AperturaCaja
    list_url = "apertura_caja_list"
    mensaje_cerrado = "La caja ya fue cerrado!"
    
    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        success_url = self.get_success_url()
        try:
            self.object = self.get_object()
           
            if self.object.esta_cerrado == True:
                raise Exception(self.mensaje_cerrado)
            else:
                self.object.esta_cerrado = True
                self.object.fecha_hora_cierre = datetime.datetime.now()
                self.object.save()
        except  Exception as e:
            self.error = e
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cierre de caja."
        context['subtitle'] = f"Desea cerrar la caja: {self.object}?" if self.page_subtitle is None else self.page_subtitle
        context['delete_button_text'] = "Cerrar"
        return context
