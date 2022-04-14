from pyexpat import model
from apps.supplies.filters import CompraFilter
from apps.supplies.forms import CompraForm, NotaDebitoRecibidaForm, OrdenCompraForm, PedidoCompraForm
from apps.supplies.models import Compra, CompraDetalle, CuotaCompra, NotaDebitoRecibida, OrdenCompra, PedidoCompra
from apps.supplies.tables import CompraDetalleTable, CompraTable, CuotaCompraTable, NotaDebitoRecibidaTable, OrdenCompraTable, PedidoCompraTable
from core.views import AnnulledView, CreateView, DetailView, ListView, UpdateView
from apps.supplies.inlines import CompraDetalleInline, CuotaCompraInline, NotaDebitoRecibidaDetalleInline, OrdenCompraDetalleInline, PedidoCompraDetalleInline

class PedidoCompraListView(ListView):
    model = PedidoCompra
    table_class = PedidoCompraTable
    search_fields = ['proveedor__razon_social',]
    update_url = 'pedido_compra_update'
    delete_url = None
    create_url = "pedido_compra_create"

class PedidoCompraCreateView(CreateView):
    model = PedidoCompra
    form_class = PedidoCompraForm
    inlines = [PedidoCompraDetalleInline]
    list_url = "pedido_compra_list"

class PedidoCompraUpdateView(UpdateView):
    model = PedidoCompra
    form_class = PedidoCompraForm
    inlines = [PedidoCompraDetalleInline]
    list_url = "pedido_compra_list"

class OrdenCompraListView(ListView):
    model = OrdenCompra
    table_class = OrdenCompraTable
    search_fields = ['proveedor__razon_social',]
    update_url = None
    delete_url = 'orden_compra_delete'
    create_url = "orden_compra_create"

class OrdenCompraCreateView(CreateView):
    model = OrdenCompra
    form_class = OrdenCompraForm
    inlines = [OrdenCompraDetalleInline]
    list_url = "orden_compra_list"

class OrdenCompraAnnulledView(AnnulledView):
    model = OrdenCompra
    list_url = "orden_compra_list"


class CompraListView(ListView):
    model = Compra
    table_class = CompraTable
    filterset_class = CompraFilter
    search_fields = ['proveedor__razon_social','comprobante','timbrado','observacion']
    update_url = None
    delete_url = "compra_delete"
    create_url = "compra_create"

class CompraCreateView(CreateView):
    model = Compra
    form_class = CompraForm
    inlines = [CompraDetalleInline,CuotaCompraInline]
    list_url = "compra_list"

    def run_form_extra_validation(self, form, inlines):
        """ ejecutar validaciones adicionales de formularios """
        compra_detalle = inlines[0]
        cuota_detalle = inlines[1]
        total_detalle = 0
        total_cuota = 0
        existe_registro = False

        for f in compra_detalle:
            total_detalle = total_detalle +f.cleaned_data.get('subtotal')
            existe_registro = True

        for f in cuota_detalle:
            if f.cleaned_data.get('monto') is not None:
                total_cuota = total_cuota + f.cleaned_data.get('monto')

        if existe_registro == False or total_detalle == 0 or total_detalle is None:
            form.add_error(None, 'Registre al menos un Detalle')
        if total_cuota is None:
            total_cuota = 0
        if form.cleaned_data.get('es_credito') and (total_detalle!=total_cuota ) :  
            form.add_error(None, 'Los montos de las cuotas difieren al total de la compra')

class CompraAnnulledView(AnnulledView):
    model = Compra
    list_url = "compra_list"
    mensaje_anulacion = "La Factura ya fue anulado."

class CompraDetailView(DetailView):
    model = Compra
    list_url = "compra_list"
    template_name = "supplies/detail_compra.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        compra_detalle = CompraDetalle.objects.filter(compra=self.object)
        cuota_compra = CuotaCompra.objects.filter(compra=self.object)
        context['compra_detalle'] = CompraDetalleTable(compra_detalle)
        context['cuota_compra'] = CuotaCompraTable(cuota_compra)
        return context

class NotaDebitoRecibidaListView(ListView):
    model = NotaDebitoRecibida
    table_class = NotaDebitoRecibidaTable
    filterset_class = None
    search_fields = ['proveedor__razon_social','comprobante','timbrado','compra__comprobante']
    list_url = "nota_debito_recibida_list"
    update_url = None
    delete_url = "nota_debito_recibida_delete"
    create_url = "nota_debito_recibida_create"

class NotaDebitoRecibidaCreateView(CreateView):
    model = NotaDebitoRecibida
    form_class = NotaDebitoRecibidaForm
    inlines = [NotaDebitoRecibidaDetalleInline]
    list_url = "nota_debito_recibida_list"

class NotaDebitoRecibidaAnnulledView(AnnulledView):
    model = NotaDebitoRecibida
    list_url = "nota_debito_recibida_list"
    mensaje_anulacion = "La Nota de Débito ya fue anulado."