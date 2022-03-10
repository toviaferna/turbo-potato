from django.urls import reverse_lazy
from apps.supplies.forms import PedidoCompraForm
from apps.supplies.mixins import FormsetInlinesMetaMixin
from apps.supplies.models import PedidoCompra
from apps.supplies.tables import PedidoCompraTable
from core.views import DeleteView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.db import models, transaction
from django.forms.formsets import all_valid
from django.core.exceptions import ValidationError
from apps.supplies.inlines import PedidoCompraDetalleInline

class CreateWithFormsetInlinesView(FormsetInlinesMetaMixin, CreateWithInlinesView):
    """
    Create view con soporte para formset inlines
    """
    def run_form_extra_validation(self, form, inlines):
        """ ejecutar validaciones adicionales de formularios """

    def run_form_extra_validation_form_master(self, form):
        """ ejecutar validaciones adicionales de formularios """
        return True


    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #initial_object = self.object
        inlines = self.construct_inlines()
        try:
            with transaction.atomic():
                if form.is_valid() and self.run_form_extra_validation_form_master(form):
                    self.object = form.save(commit=False)
                    form_validated = True
                else:
                    form_validated = False
                # Loop through inlines to set master instance
                for inline in inlines:
                    inline.instance = form.instance

                if all_valid(inlines) and form_validated:
                    response = self.forms_valid(form, inlines)
                    self.run_form_extra_validation(form, inlines)
                    if not form.errors and response:
                        return response
                raise ValidationError('Error')
        except ValidationError:
            pass
        #self.object = initial_object
        return self.forms_invalid(form, inlines)
class UpdateWithFormsetInlinesView(FormsetInlinesMetaMixin, UpdateWithInlinesView):
    """
    Update view con soporte para formset inlines
    """

    def run_form_extra_validation(self, form, inlines):
        """ ejecutar validaciones adicionales de formularios """

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        initial_object = self.object
        inlines = self.construct_inlines()
        try:
            with transaction.atomic():
                if form.is_valid():
                    self.object = form.save(commit=False)
                    form_validated = True
                else:
                    form_validated = False
                # Loop through inlines to set master instance
                for inline in inlines:
                    inline.instance = form.instance

                if all_valid(inlines) and form_validated:
                    response = self.forms_valid(form, inlines)
                    self.run_form_extra_validation(form, inlines)
                    if not form.errors and response:
                        return response
                raise ValidationError('Error')
        except ValidationError:
            pass
        self.object = initial_object
        return self.forms_invalid(form, inlines)

class PedidoCompraListView(ListView):
    model = PedidoCompra
    table_class = PedidoCompraTable
    search_fields = ['proveedor__razon_social',]
    update_url = 'pedido_compra_update'
    delete_url = None #'pedido_compra_delete'
    create_url = "pedido_compra_create"
    page_title = "Pedidos de compras"


class PedidoCompraCreateView(LoginRequiredMixin,CreateWithFormsetInlinesView):
    model = PedidoCompra
    form_class = PedidoCompraForm
    template_name = 'generic/edit.html'
    inlines = [PedidoCompraDetalleInline]

    def get_success_url(self):
        return reverse_lazy('pedido_compra_list')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['list_url'] = 'pedico_compra_list'
        return context

class PedidoCompraUpdateView(LoginRequiredMixin,UpdateWithFormsetInlinesView):
    model = PedidoCompra
    form_class = PedidoCompraForm
    template_name = 'generic/edit.html'
    inlines = [PedidoCompraDetalleInline]

    def get_success_url(self):
        return reverse_lazy('pedido_compra_list')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['list_url'] = 'pedico_compra_list'
        return context
