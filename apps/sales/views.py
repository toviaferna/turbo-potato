import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Max
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from num2words import num2words
from xhtml2pdf import pisa

from apps.finance.models import Persona
from apps.sales import filters, forms, inlines, models, tables
from core import views
from core.utils import link_callback


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
    search_fields = [
        "cuenta_salida__descripcion",
        "cuenta_entrada__descripcion",
        "comprobante",
    ]
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
    search_fields = ["cliente__razon_social", "comprobante", "timbrado", "observacion"]
    create_url = "venta_create"
    delete_url = "venta_delete"
    download_url = "venta_download"


class VentaCreateView(views.CreateView):
    model = models.Venta
    form_class = forms.VentaForm
    inlines = [inlines.VentaDetalleInline, inlines.CuotaVentaInline]
    list_url = "venta_list"

    class Media:
        js = ("assets/js/widgets.js",)

    def get_initial(self):

        initial = super().get_initial()
        
        # Obtener el timbrado vigente
        timbrado_vigente = models.Timbrado.objects.filter(
            es_vigente=True,
            tipo_documento=1
        ).first()
        
        if timbrado_vigente:
            # Obtener el último número de comprobante para este timbrado
            ultimo_comprobante = self.model.objects.filter(
                comprobante__startswith=(
                    f"{timbrado_vigente.punto_expedicion.establecimiento.numero}-"
                    f"{timbrado_vigente.punto_expedicion.numero}"
                )
            ).aggregate(
                Max('comprobante')
            )['comprobante__max']
            
            if ultimo_comprobante:
                # Extraer el último número y aumentarlo en 1
                ultimo_numero = int(ultimo_comprobante.split('-')[2])
                siguiente_numero = ultimo_numero + 1
            else:
                # Si no hay comprobantes previos, comenzar desde el número inicial del timbrado
                siguiente_numero = timbrado_vigente.numero_inicial
                
            # Formar el nuevo número de comprobante
            nuevo_comprobante = (
                f"{timbrado_vigente.punto_expedicion.establecimiento.numero}-"
                f"{timbrado_vigente.punto_expedicion.numero}-"
                f"{str(siguiente_numero).zfill(7)}"
            )
            
            initial['comprobante'] = nuevo_comprobante
            initial['fecha_documento'] = datetime.date.today()
            
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Verificar si hay un timbrado vigente
        timbrado_vigente = models.Timbrado.objects.filter(
            es_vigente=True,
            tipo_documento=1
        ).first()

        # Si no hay timbrado vigente, agregar un mensaje de error en el contexto
        if not timbrado_vigente:
            context['error_message'] = "No hay un timbrado vigente disponible. No se pueden crear ventas."
        
        return context



    def run_form_extra_validation_form_master(self, form):
        apertura_caja = (
            models.AperturaCaja.objects.filter(esta_cerrado=False)
            .order_by("-pk")[:1]
            .first()
        )
        if apertura_caja is None:
            form.add_error(None, "No existe una apertura de Caja en estado ABIERTO")
            return False
        return True

    def run_form_extra_validation(self, form, inlines):
        venta_detalle = inlines[0]
        cuota_detalle = inlines[1]
        total_detalle = 0
        total_cuota = 0
        existe_registro = False

        for f in venta_detalle:
            total_detalle += f.cleaned_data.get("subtotal")
            existe_registro = True

        for f in cuota_detalle:
            valor = 0
            if f.cleaned_data.get("monto") is None:
                valor = 0
            else:
                valor = f.cleaned_data.get("monto")
            total_cuota += valor

        if existe_registro == False or total_detalle == 0 or total_detalle is None:
            form.add_error(None, "Registre al menos un Detalle")

        if form.cleaned_data.get("es_credito") and (total_detalle != total_cuota):
            form.add_error(
                None, "Los montos de las cuotas difieren al total de la venta"
            )


class VentaAnnulledView(views.AnnulledView):
    model = models.Venta
    list_url = "venta_list"
    mensaje_anulacion = "La Venta ya fue anulado."

class VentaDetailView(views.DetailView):
    model = models.Venta
    list_url = "venta_list"
    template_name = "sales/detail_venta.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venta_detalle = models.VentaDetalle.objects.filter(venta=self.object)
        cuota_venta = models.CuotaVenta.objects.filter(venta=self.object)
        context["venta_detalle"] = tables.VentaDetalleTable(venta_detalle)
        context["cuota_venta"] = tables.CuotaVentaTable(cuota_venta)
        return context


def download_view(request, pk):
    """"""
    template_path = "sales/invoice.html"
    object = models.Venta.objects.get(pk=pk)
    detalles = object.ventadetalle_set.all()

    context = {
        "object": object,
        "number_to_words": str(num2words(object.total, lang="es")).capitalize,
        "invoice_css_dir": settings.EXPORT_PDF_CSS.get("invoice_css"),
        "invoice_img_dir": settings.EXPORT_PDF_CSS.get("invoice_img"),
        "detalles": detalles,
        "empresa": settings.EMPRESA
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{object.comprobante}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # if error then show some funy view

    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


class NotaCreditoEmitidaListView(views.ListView):
    model = models.NotaCreditoEmitida
    table_class = tables.NotaCreditoEmitidaTable
    search_fields = [
        "cliente__razon_social",
        "comprobante",
        "timbrado",
        "venta__comprobante",
    ]
    create_url = "nota_credito_emitida_create"
    delete_url = "nota_credito_emitida_delete"


class NotaCreditoEmitidaCreateView(views.CreateView):
    model = models.NotaCreditoEmitida
    form_class = forms.NotaCreditoEmitidaForm
    inlines = [inlines.NotaCreditoEmitidaDetalleInline]
    list_url = "nota_credito_emitida_list"

    def get_initial(self):

        initial = super().get_initial()
        
        # Obtener el timbrado vigente
        timbrado_vigente = models.Timbrado.objects.filter(
            es_vigente=True,
            tipo_documento=2
        ).first()
        
        if timbrado_vigente:
            # Obtener el último número de comprobante para este timbrado
            ultimo_comprobante = self.model.objects.filter(
                comprobante__startswith=(
                    f"{timbrado_vigente.punto_expedicion.establecimiento.numero}-"
                    f"{timbrado_vigente.punto_expedicion.numero}"
                )
            ).aggregate(
                Max('comprobante')
            )['comprobante__max']
            
            if ultimo_comprobante:
                # Extraer el último número y aumentarlo en 1
                ultimo_numero = int(ultimo_comprobante.split('-')[2])
                siguiente_numero = ultimo_numero + 1
            else:
                # Si no hay comprobantes previos, comenzar desde el número inicial del timbrado
                siguiente_numero = timbrado_vigente.numero_inicial
                
            # Formar el nuevo número de comprobante
            nuevo_comprobante = (
                f"{timbrado_vigente.punto_expedicion.establecimiento.numero}-"
                f"{timbrado_vigente.punto_expedicion.numero}-"
                f"{str(siguiente_numero).zfill(7)}"
            )
            
            initial['comprobante'] = nuevo_comprobante
            initial['fecha_documento'] = datetime.date.today()
            
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Verificar si hay un timbrado vigente
        timbrado_vigente = models.Timbrado.objects.filter(
            es_vigente=True,
            tipo_documento=2
        ).first()

        # Si no hay timbrado vigente, agregar un mensaje de error en el contexto
        if not timbrado_vigente:
            context['error_message'] = "No hay un timbrado vigente disponible. No se pueden crear nota de credito."
        
        return context


class NotaCreditoEmitidaAnnulledView(views.AnnulledView):
    model = models.NotaCreditoEmitida
    list_url = "nota_credito_emitida_list"
    mensaje_anulacion = "La Nota de Crédito ya fue anulado."

class NotaCreditoEmitidaDetailView(views.DetailView):
    model = models.NotaCreditoEmitida
    list_url = "nota_credito_emitida_list"
    template_name = "sales/detail_nota_credito.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nota_credito_detalle = models.NotaCreditoEmitidaDetalle.objects.filter(nota_credito_emitida=self.object)
        context["nota_credito_detalle"] = tables.NotaCreditoDetalleTable(nota_credito_detalle)
        return context

class NotaDebitoEmitidaListView(views.ListView):
    model = models.NotaDebitoEmitida
    table_class = tables.NotaDebitoEmitidaTable
    search_fields = [
        "cliente__razon_social",
        "comprobante",
        "timbrado",
        "venta__comprobante",
    ]
    create_url = "nota_debito_emitida_create"
    delete_url = "nota_debito_emitida_delete"


class NotaDebitoEmitidaCreateView(views.CreateView):
    model = models.NotaDebitoEmitida
    form_class = forms.NotaDebitoEmitidaForm
    inlines = [inlines.NotaDebitoEmitidaDetalleInline]
    list_url = "nota_debito_emitida_list"
    
    def get_initial(self):

        initial = super().get_initial()
        
        # Obtener el timbrado vigente
        timbrado_vigente = models.Timbrado.objects.filter(
            es_vigente=True,
            tipo_documento=3
        ).first()
        
        if timbrado_vigente:
            # Obtener el último número de comprobante para este timbrado
            ultimo_comprobante = self.model.objects.filter(
                comprobante__startswith=(
                    f"{timbrado_vigente.punto_expedicion.establecimiento.numero}-"
                    f"{timbrado_vigente.punto_expedicion.numero}"
                )
            ).aggregate(
                Max('comprobante')
            )['comprobante__max']
            
            if ultimo_comprobante:
                # Extraer el último número y aumentarlo en 1
                ultimo_numero = int(ultimo_comprobante.split('-')[2])
                siguiente_numero = ultimo_numero + 1
            else:
                # Si no hay comprobantes previos, comenzar desde el número inicial del timbrado
                siguiente_numero = timbrado_vigente.numero_inicial
                
            # Formar el nuevo número de comprobante
            nuevo_comprobante = (
                f"{timbrado_vigente.punto_expedicion.establecimiento.numero}-"
                f"{timbrado_vigente.punto_expedicion.numero}-"
                f"{str(siguiente_numero).zfill(7)}"
            )
            
            initial['comprobante'] = nuevo_comprobante
            initial['fecha_documento'] = datetime.date.today()
            
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Verificar si hay un timbrado vigente
        timbrado_vigente = models.Timbrado.objects.filter(
            es_vigente=True,
            tipo_documento=3
        ).first()

        # Si no hay timbrado vigente, agregar un mensaje de error en el contexto
        if not timbrado_vigente:
            context['error_message'] = "No hay un timbrado vigente disponible. No se pueden crear nota de credito."
        
        return context


class NotaDebitoEmitidaAnnulledView(views.AnnulledView):
    model = models.NotaDebitoEmitida
    list_url = "nota_debito_emitida_list"
    mensaje_anulacion = "La Nota de Débito ya fue anulado."

class NotaDebitoEmitidaDetailView(views.DetailView):
    model = models.NotaDebitoEmitida
    list_url = "nota_debito_emitida_list"
    template_name = "sales/detail_nota_debito.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nota_debito_detalle = models.NotaDebitoEmitidaDetalle.objects.filter(nota_debito_emitida=self.object)
        context["nota_debito_detalle"] = tables.NotaDebitoDetalleTable(nota_debito_detalle)
        return context

class CobroListView(views.ListView):
    model = models.Cobro
    table_class = tables.CobroTable
    search_fields = ["cliente__razon_social", "comprobante", "cobrador__razon_social"]
    create_url = "cobro_selection"
    delete_url = "cobro_delete"


class CobroPersonaSelectionListView(views.SelectionListView):
    model = Persona
    table_class = tables.CobroPersonaSelectionTable
    search_fields = ["razon_social", "documento"]
    next_url = "cobro_create"
    back_url = "cobro_list"
    list_url = "cobro_list"
    selection_title = "Seleccione un registro para continuar"
    params_name = "cliente"
    queryset = Persona.objects.filter(es_cliente=True)
    export_button = False


class CobroCreateView(views.CreateView):
    model = models.Cobro
    form_class = forms.CobroForm
    inlines = [inlines.CobroDetalleInline, inlines.CobroMedioInline]
    list_url = "cobro_list"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.request.GET.get("cliente", None):
            form.fields["cliente"].initial = self.request.GET.get("cliente", None)
            form.fields["cliente"].widget.attrs.update(
                {"readonly": True, "style": "pointer-events:none;"}
            )
        return form

    def run_form_extra_validation(self, form, inlines):
        """ejecutar validaciones adicionales de formularios"""

        cobro_detalle_inline = inlines[0]
        medio_cobro_detalle_inline = inlines[1]

        existe_seleccionado = False
        total_cuota = 0
        for f in cobro_detalle_inline:
            if f.cleaned_data.get("check"):
                existe_seleccionado = True
                if f.cleaned_data.get("cancelacion") is not None:
                    total_cuota = total_cuota + f.cleaned_data.get("cancelacion")

        total_medio_cobro = 0
        for f in medio_cobro_detalle_inline:
            if f.cleaned_data.get("monto") is not None:
                total_medio_cobro = total_medio_cobro + f.cleaned_data.get("monto")
        monto_a_saldar_valor = form.cleaned_data["monto_a_saldar"]
        if existe_seleccionado == False:
            form.add_error(None, "Seleccione al menos un detalle a cobrar")
        if total_cuota != monto_a_saldar_valor:
            form.add_error(
                "monto_a_saldar",
                "El Monto A Saldar difiere de la suma de las cancelaciones de las cuotas",
            )
        if total_medio_cobro != monto_a_saldar_valor:
            form.add_error(
                "monto_a_saldar",
                "El Monto A Saldar difiere de la suma de los medios de cobros",
            )

    def get_inlines(self):
        initial = [
            {
                "cuota_venta": x,
                "check": False,
                "comprobante": x.venta.comprobante,
                "monto": round(x.monto),
                "saldo": round(x.saldo),
                "cancelacion": 0,
            }
            for x in models.CuotaVenta.objects.filter(
                venta__es_vigente=True,
                venta__cliente__pk=self.request.GET.get("cliente"),
            ).exclude(saldo=0)
        ]
        cobro_detalle_inline = self.inlines[0]
        cobro_detalle_inline.initial = initial
        cobro_detalle_inline.factory_kwargs["extra"] = len(initial)
        cobro_detalle_inline.factory_kwargs["can_delete"] = False
        return self.inlines


class CobroAnnulledView(views.AnnulledView):
    model = models.Cobro
    list_url = "cobro_list"
    mensaje_anulacion = "El Cobro ya fue anulado."

class LibroVentaListView(views.ListView):
    model = models.Venta
    filterset_class = filters.LibroVentaFilter
    table_class = tables.LibroVentaTable
    search_fields = ['comprobante','cliente__razon_social','deposito__descripcion'] #context?
    page_title = "Libro de ventas"
    export_page_orientation = "landscape"

class EstablecimientoListView(views.ListView):
    model = models.Establecimiento
    table_class = tables.EstablecimientoTable
    search_fields = ['descripcion']
    update_url = 'establecimiento_update'
    delete_url = 'establecimiento_delete'
    create_url = 'establecimiento_create'

class EstablecimientoCreateView(views.CreateView):
    form_class = forms.EstablecimientoForm
    model = models.Establecimiento
    list_url = "establecimiento_list"

class EstablecimientoUpdateView(views.UpdateView):
    form_class = forms.EstablecimientoForm
    model = models.Establecimiento
    list_url = "establecimiento_list"

class EstablecimientoDeleteView(views.DeleteView):
    model = models.Establecimiento
    list_url = "establecimiento_list"

class PuntoExpedicionListView(views.ListView):
    model = models.PuntoExpedicion
    table_class = tables.PuntoExpedicionTable
    search_fields = ['descripcion',]
    update_url = 'punto_expedicion_update'
    delete_url = 'punto_expedicion_delete'
    create_url = 'punto_expedicion_create'

class PuntoExpedicionCreateView(views.CreateView):
    form_class = forms.PuntoExpedicionForm
    model = models.PuntoExpedicion
    list_url = "punto_expedicion_list"

class PuntoExpedicionUpdateView(views.UpdateView):
    form_class = forms.PuntoExpedicionForm
    model = models.PuntoExpedicion
    list_url = "punto_expedicion_list"

class PuntoExpedicionDeleteView(views.DeleteView):
    model = models.PuntoExpedicion
    list_url = "punto_expedicion_list"

class TipoDocumentoListView(views.ListView):
    model = models.TipoDocumento
    table_class = tables.TipoDocumentoTable
    search_fields = ['descripcion',]
    update_url = 'tipo_documento_update'
    delete_url = 'tipo_documento_delete'
    create_url = 'tipo_documento_create'

class TipoDocumentoCreateView(views.CreateView):
    form_class = forms.TipoDocumentoForm
    model = models.TipoDocumento
    list_url = "tipo_documento_list"

class TipoDocumentoUpdateView(views.UpdateView):
    form_class = forms.TipoDocumentoForm
    model = models.TipoDocumento
    list_url = "tipo_documento_list"

class TipoDocumentoDeleteView(views.DeleteView):
    model = models.TipoDocumento
    list_url = "tipo_documento_list"

class TimbradoListView(views.ListView):
    model = models.Timbrado
    table_class = tables.TimbradoTable
    search_fields = ['numero',]
    update_url = 'timbrado_update'
    delete_url = 'timbrado_delete'
    create_url = 'timbrado_create'

class TimbradoCreateView(views.CreateView):
    form_class = forms.TimbradoForm
    model = models.Timbrado
    list_url = "timbrado_list"

class TimbradoUpdateView(views.UpdateView):
    form_class = forms.TimbradoForm
    model = models.Timbrado
    list_url = "timbrado_list"

class TimbradoDeleteView(views.DeleteView):
    model = models.Timbrado
    list_url = "timbrado_list"

