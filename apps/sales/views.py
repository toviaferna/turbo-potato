import datetime

from apps.sales import filters, forms, inlines, models, tables
from core import views
from django.db import transaction
from django.http import HttpResponseRedirect


# Create your views here.
class AperturaCajaListView(views.ListView):
    model = models.AperturaCaja
    table_class = tables.AperturaCajaTable
    filterset_class = filters.AperturaCajaFilter
    search_fields = ["empleado__razon_social", "observacion"]
    update_url = None
    create_url = "apertura_caja_create"  #'apertura_caja_create'
    delete_url = "apertura_caja_delete"  #'apertura_caja_delete'


class AperturaCajaCreateView(views.CreateView):
    form_class = forms.AperturaCajaCreateForm
    model = models.AperturaCaja
    list_url = "apertura_caja_list"


class AperturaCajaDeleteView(views.DeleteView):
    model = models.AperturaCaja
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
        except Exception as e:
            self.error = e
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cierre de caja."
        context["subtitle"] = (
            f"Desea cerrar la caja: {self.object}?"
            if self.page_subtitle is None
            else self.page_subtitle
        )
        context["delete_button_text"] = "Cerrar"
        return context


class ArqueoListView(views.ListView):
    model = models.Arqueo
    table_class = tables.ArqueoTable
    search_fields = ["empleado__razon_social", "observacion"]
    update_url = None
    create_url = "arqueo_create"
    delete_url = "arqueo_delete"

class ArqueoCreateView(views.CreateView):
    model = models.Arqueo
    form_class = forms.ArqueoForm
    list_url = "arqueo_list"

class ArqueoDeleteView(views.DeleteView):
    model = models.Arqueo
    list_url = "arqueo_list"

class TransferenciaCuentaListView(views.ListView):
    model = models.TransferenciaCuenta
    table_class = tables.TransferenciaCuentaTable
    search_fields = ['cuenta_salida__descripcion','cuenta_entrada__descripcion','comprobante']
    update_url = None
    create_url = "transferencia_cuenta_create"
    delete_url = "transferencia_cuenta_delete"

class TransferenciaCuentaCreateView(views.CreateView):
    model = models.TransferenciaCuenta
    form_class = forms.TransferenciaCuentaForm
    list_url = "transferencia_cuenta_list"

class TransferenciaCuentaAnnulledView(views.AnnulledView):
    model = models.TransferenciaCuenta
    list_url = "transferencia_cuenta_list"
    mensaje_anulacion = "La Transferencia ya fue anulado."

class VentaListView(views.ListView):
    model = models.Venta
    table_class = tables.VentaTable
    search_fields = ['cliente__razon_social','comprobante','timbrado','observacion']
    create_url = "venta_create"
    delete_url = "venta_delete"
    download_url = None#"venta_download"

class VentaCreateView(views.CreateView):
    model = models.Venta
    form_class = forms.VentaForm
    inlines = [inlines.VentaDetalleInline, inlines.CuotaVentaInline]
    list_url = "venta_list"
   
    class Media:
        js = ("assets/js/widgets.js",)

    def run_form_extra_validation_form_master(self,form):
        apertura_caja = models.AperturaCaja.objects.filter(esta_cerrado = False).order_by('-pk')[:1].first()
        if apertura_caja is None:
            form.add_error(None, 'No existe una apertura de Caja en estado ABIERTO')
            return False
        return True
    
    def run_form_extra_validation(self, form, inlines):
        venta_detalle = inlines[0]
        cuota_detalle = inlines[1]
        total_detalle = 0
        total_cuota = 0
        existe_registro = False

        for f in venta_detalle:
            total_detalle += f.cleaned_data.get('subtotal')
            existe_registro = True

        for f in cuota_detalle:
            valor = 0 
            if f.cleaned_data.get('monto') is None:
                valor = 0
            else:
                valor = f.cleaned_data.get('monto')
            total_cuota += valor

        if existe_registro == False or total_detalle == 0 or total_detalle is None:
            form.add_error(None, 'Registre al menos un Detalle')
        
        if form.cleaned_data.get('es_credito') and (total_detalle!=total_cuota) :  
            form.add_error(None, 'Los montos de las cuotas difieren al total de la venta')

class VentaAnnulledView(views.AnnulledView):
    model = models.Venta
    list_url = "venta_list"
    mensaje_anulacion = "La Venta ya fue anulado."
