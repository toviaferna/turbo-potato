from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from apps.supplies import forms, inlines, models, tables
from apps.supplies.filters import (CompraFilter, LibroCompraFilter,
                                   OrdenCompraFilter, PedidoCompraFilter)
from core import views


class PedidoCompraListView(views.ListView):
    model = models.PedidoCompra
    table_class = tables.PedidoCompraTable
    filterset_class = PedidoCompraFilter
    search_fields = [
        "proveedor__razon_social",
    ]
    delete_url = "pedido_compra_delete"
    #update_url = "pedido_compra_update"
    create_url = "pedido_compra_create"


class PedidoCompraCreateView(views.CreateView):
    model = models.PedidoCompra
    form_class = forms.PedidoCompraForm
    inlines = [inlines.PedidoCompraDetalleInline]
    list_url = "pedido_compra_list"


class PedidoCompraUpdateView(views.UpdateView):
    model = models.PedidoCompra
    form_class = forms.PedidoCompraForm
    inlines = [inlines.PedidoCompraDetalleInline]
    list_url = "pedido_compra_list"

class PedidoCompraAnnulledView(views.AnnulledView):
    model = models.PedidoCompra
    list_url = "pedido_compra_list"

class PedidoCompraDetailView(views.DetailView):
    model = models.PedidoCompra
    list_url = "pedido_compra_list"
    template_name = "supplies/detail_pedido_compra.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedido_compra_detalle = models.PedidoCompraDetalle.objects.filter(pedido_compra=self.object)
        context["pedido_compra_detalle"] = tables.PedidoCompraDetalleTable(pedido_compra_detalle)
        return context

class OrdenCompraUpdateView(views.UpdateView):
    model = models.OrdenCompra
    form_class = forms.OrdenCompraForm
    inlines = [inlines.OrdenCompraDetalleInline]
    list_url = "orden_compra_list"
    


class OrdenCompraListView(views.ListView):
    model = models.OrdenCompra
    table_class = tables.OrdenCompraTable
    filterset_class = OrdenCompraFilter
    search_fields = [
        "proveedor__razon_social",
    ]
    delete_url = "orden_compra_delete"
    create_url = "orden_compra_create"
    update_url = "orden_compra_update"


class OrdenCompraCreateView(views.CreateView):
    model = models.OrdenCompra
    form_class = forms.OrdenCompraForm
    inlines = [inlines.OrdenCompraDetalleInline]
    list_url = "orden_compra_list"


class OrdenCompraAnnulledView(views.AnnulledView):
    model = models.OrdenCompra
    list_url = "orden_compra_list"

class OrdenCompraDetailView(views.DetailView):
    model = models.OrdenCompra
    list_url = "orden_compra_list"
    template_name = "supplies/detail_orden_compra.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orden_compra_detalle = models.OrdenCompraDetalle.objects.filter(orden_compra=self.object)
        context["orden_compra_detalle"] = tables.OrdenCompraDetalleTable(orden_compra_detalle)
        context["orden"] = self.object
        return context

class CompraListView(views.ListView): 
    model = models.Compra
    table_class = tables.CompraTable
    filterset_class = CompraFilter
    search_fields = [
        "proveedor__razon_social",
        "comprobante",
        "timbrado",
        "observacion",
    ]
    delete_url = "compra_delete"
    create_url = "compra_create"


class CompraCreateView(views.CreateView):
    model = models.Compra
    form_class = forms.CompraForm
    inlines = [inlines.CompraDetalleInline, inlines.CuotaCompraInline]
    list_url = "compra_list"

    class Media:
        js = ("assets/js/widgets.js",)

    def get_initial(self):
        initial = super().get_initial()
        orden_compra = self.get_orden_compra()
        if orden_compra:
            initial['proveedor'] = orden_compra.proveedor
            initial['fecha_documento'] = orden_compra.fecha_documento
            initial['observacion'] = f"Compra generada desde Orden de Compra Nro. {orden_compra.pk}"
        return initial

    def get_orden_compra(self):
        orden_pk = self.kwargs.get('orden_pk')
        if orden_pk:
            return get_object_or_404(models.OrdenCompra, pk=orden_pk)
        return None

    def run_form_extra_validation(self, form, inlines):
        """ejecutar validaciones adicionales de formularios"""
        compra_detalle = inlines[0]
        cuota_detalle = inlines[1]
        total_detalle = 0
        total_cuota = 0
        existe_registro = False

        for f in compra_detalle:
            total_detalle = total_detalle + f.cleaned_data.get("subtotal")
            existe_registro = True

        for f in cuota_detalle:
            if f.cleaned_data.get("monto") is not None:
                total_cuota = total_cuota + f.cleaned_data.get("monto")

        if existe_registro == False or total_detalle == 0 or total_detalle is None:
            form.add_error(None, "Registre al menos un Detalle")
        if total_cuota is None:
            total_cuota = 0
        if form.cleaned_data.get("es_credito") and (total_detalle != total_cuota):
            form.add_error(
                None, "Los montos de las cuotas difieren al total de la compra"
            )


class CompraAnnulledView(views.AnnulledView):
    model = models.Compra
    list_url = "compra_list"
    mensaje_anulacion = "La Factura ya fue anulado."


class CompraDetailView(views.DetailView):
    model = models.Compra
    list_url = "compra_list"
    template_name = "supplies/detail_compra.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        compra_detalle = models.CompraDetalle.objects.filter(compra=self.object)
        cuota_compra = models.CuotaCompra.objects.filter(compra=self.object)
        context["compra_detalle"] = tables.CompraDetalleTable(compra_detalle)
        context["cuota_compra"] = tables.CuotaCompraTable(cuota_compra)
        return context


class NotaDebitoRecibidaListView(views.ListView):
    model = models.NotaDebitoRecibida
    table_class = tables.NotaDebitoRecibidaTable
    filterset_class = None
    search_fields = [
        "proveedor__razon_social",
        "comprobante",
        "timbrado",
        "compra__comprobante",
    ]
    list_url = "nota_debito_recibida_list"
    delete_url = "nota_debito_recibida_delete"
    create_url = "nota_debito_recibida_create"


class NotaDebitoRecibidaCreateView(views.CreateView):
    model = models.NotaDebitoRecibida
    form_class = forms.NotaDebitoRecibidaForm
    inlines = [inlines.NotaDebitoRecibidaDetalleInline]
    list_url = "nota_debito_recibida_list"

    class Media:
        js = ("assets/js/widgets.js",)


class NotaDebitoRecibidaAnnulledView(views.AnnulledView):
    model = models.NotaDebitoRecibida
    list_url = "nota_debito_recibida_list"
    mensaje_anulacion = "La Nota de Débito ya fue anulado."


class NotaCreditoRecibidaListView(views.ListView):
    model = models.NotaCreditoRecibida
    table_class = tables.NotaCreditoRecibidaTable
    filterset_class = None
    search_fields = [
        "proveedor__razon_social",
        "comprobante",
        "timbrado",
        "compra__comprobante",
    ]
    list_url = "nota_credito_recibida_list"
    delete_url = "nota_credito_recibida_delete"
    create_url = "nota_credito_recibida_create"


class NotaCreditoRecibidaCreateView(views.CreateView):
    model = models.NotaCreditoRecibida
    form_class = forms.NotaCreditoRecibidaForm
    inlines = [inlines.NotaCreditoRecibidaDetalleInline]
    list_url = "nota_credito_recibida_list"

    class Media:
        js = ("assets/js/widgets.js",)


class NotaCreditoRecibidaAnnulledView(views.AnnulledView):
    model = models.NotaCreditoRecibida
    list_url = "nota_credito_recibida_list"
    mensaje_anulacion = "La Nota de Crédito ya fue anulado."


class LibroCompraListView(views.ListView):
    model = models.Compra
    filterset_class = LibroCompraFilter
    table_class = tables.LibroCompraTable
    page_title = "Libro de compras"
    search_fields = ["comprobante", "proveedor__razon_social", "deposito__descripcion"]
    export_page_orientation = "landscape"
