from django.forms import NumberInput, widgets
from extra_views import InlineFormSetFactory

from apps.supplies import forms, models
from core.widgets import AutocompleteSelect


class PedidoCompraDetalleInline(InlineFormSetFactory):
    model = models.PedidoCompraDetalle
    form_class = forms.PedidoCompraDetalleForm
    factory_kwargs = {
        "extra": 1,
        "widgets": {
            "cantidad": NumberInput(
                attrs={
                    "class": "text-right",
                    "wrapper_class": "col-sm-2",
                }
            ),
            "item": AutocompleteSelect(
                url="producto_normal_autocomplete",
                attrs={
                    "data-placeholder": "Buscar por descripcion, categoria, marca.",
                    "wrapper_class": "col-sm-10",
                    "data-width": "100%",
                },
            ),
        }
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

    def __init__(self, *args, **kwargs):
        self.view = kwargs.pop('view', None)  # Extraemos la vista de kwargs
        super().__init__(*args, **kwargs)

    def get_initial(self):
        initial = []
        if self.view:
            orden_compra = self.view.get_orden_compra()
            if orden_compra:
                # Imprime para debug
                print(f"Orden de compra encontrada: {orden_compra.pk}")
                detalles = orden_compra.ordencompradetalle_set.all()
                print(f"Cantidad de detalles: {detalles.count()}")
                
                for item in detalles:
                    initial.append({
                        "item": item.item,
                        "cantidad": item.cantidad,
                        "costo": item.precio,
                        "porcentaje_impuesto": item.item.tipo_impuesto.porcentaje,
                    })
        
        print(f"Initial data: {initial}")  # Debug
        return initial
    
    def get_factory_kwargs(self):
        kwargs = super().get_factory_kwargs()
        initial_data = self.get_initial()
        if initial_data:
            # Configuramos el número exacto de formularios basado en los datos iniciales
            kwargs.update({
                'extra': 0,
                'min_num': len(initial_data),
                #'max_num': len(initial_data),
                #'absolute_max': len(initial_data) + 10,  # Por si necesitas añadir más después
            })
        return kwargs

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
            "item": AutocompleteSelect(
                url="producto_autocomplete",
                attrs={
                    "data-placeholder": "Buscar por descripcion, categoria, marca.",
                    "wrapper_class": "col-sm-4",
                    "data-item-select": True,
                },
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
            "item": AutocompleteSelect(
                url="producto_autocomplete",
                attrs={
                    "data-placeholder": "Buscar por descripcion, categoria, marca.",
                    "wrapper_class": "col-sm-4",
                    "data-item-select": True,
                },
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
