from apps.supplies import forms, models
from core.widgets import AutocompleteSelect, ItemCustomSelect
from django.forms import widgets
from extra_views import InlineFormSetFactory


class PedidoCompraDetalleInline(InlineFormSetFactory):
    model = models.PedidoCompraDetalle
    form_class = forms.PedidoCompraDetalleForm
    factory_kwargs = {
        "extra": 1,
    }
    fields = ["item", "cantidad"]


class OrdenCompraDetalleInline(InlineFormSetFactory):
    model = models.OrdenCompraDetalle
    form_class = forms.OrdenCompraDetalleForm
    factory_kwargs = {
        "extra": 1,
    }
    fields = ["item", "cantidad", "precio", "descuento"]


class CompraDetalleInline(InlineFormSetFactory):
    model = models.CompraDetalle
    form_class = forms.CompraDetalleForm
    factory_kwargs = {
        "extra": 1,
        "widgets": {
            "item": AutocompleteSelect(
                url="producto_normal_autocomplete",
                attrs={
                    "data-placeholder": "Buscar por descripcion, categoria, marca.",
                    "wrapper_class": "col-sm-4",
                    "data-item-select": True,
                },
            ),
            "cantidad": widgets.NumberInput(
                attrs={
                    "wrapper_class": "col-sm-1",
                    "class": "text-right",
                }
            ),
            "costo": widgets.NumberInput(
                attrs={
                    "class": "text-right item-costo",
                }
            ),
            "porcentaje_impuesto": widgets.NumberInput(
                attrs={
                    "class": "text-right item-porcentaje-impuesto",
                }
            ),
        },
    }
    fields = [
        "item",
        "cantidad",
        "costo",
        "porcentaje_impuesto",
    ]


class CuotaCompraInline(InlineFormSetFactory):
    model = models.CuotaCompra
    form_class = forms.CuotaCompraForm
    factory_kwargs = {"extra": 1}
    fields = ["fecha_vencimiento", "monto"]


class NotaDebitoRecibidaDetalleInline(InlineFormSetFactory):
    model = models.NotaDebitoRecibidaDetalle
    form_class = forms.NotaDebitoRecibidaDetalleForm
    factory_kwargs = {
        "extra": 1,
        "widgets": {
            "item": ItemCustomSelect(
                attrs={
                    "wrapper_class": "col-sm-3",
                    "data-item-select": True,
                }
            ),
            "porcentaje_impuesto": widgets.NumberInput(
                attrs={
                    "class": "text-right item-porcentaje-impuesto",
                }
            ),
            "valor": widgets.NumberInput(
                attrs={
                    "class": "text-right item-costo",
                }
            ),
            "cantidad": widgets.NumberInput(
                attrs={
                    "wrapper_class": "col-sm-1",
                }
            ),
        },
    }
    fields = [
        "item",
        "cantidad",
        "valor",
        "porcentaje_impuesto",
    ]


class NotaCreditoRecibidaDetalleInline(InlineFormSetFactory):
    model = models.NotaCreditoRecibidaDetalle
    form_class = forms.NotaCreditoRecibidaDetalleForm
    factory_kwargs = {
        "extra": 1,
        "widgets": {
            "item": ItemCustomSelect(
                attrs={
                    "wrapper_class": "col-sm-3",
                    "data-item-select": True,
                }
            ),
            "porcentaje_impuesto": widgets.NumberInput(
                attrs={
                    "class": "text-right item-porcentaje-impuesto",
                }
            ),
            "valor": widgets.NumberInput(
                attrs={
                    "class": "text-right item-costo",
                }
            ),
            "cantidad": widgets.NumberInput(
                attrs={
                    "wrapper_class": "col-sm-1",
                }
            ),
        },
    }
    fields = [
        "es_devolucion",
        "item",
        "cantidad",
        "valor",
        "porcentaje_impuesto",
    ]
