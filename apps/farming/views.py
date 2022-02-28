from django.shortcuts import render
from django_tables2 import SingleTableMixin
from apps.farming.tables import FincaTable
from .models import Finca
from apps.mixins import SearchViewMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.views.generic.list import ListView

# FINCA
class FincaListView(LoginRequiredMixin,SearchViewMixin, SingleTableMixin, ListView):
    model = Finca
    table_class = FincaTable
    paginate_by = 6
    search_fields = ['descripcion','ubicacion']
    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'home'
        context['delete_url'] = 'home'
        context['segment'] = 'finca'
        return context
""" 
class FincaCreateView(LoginRequiredMixin,CreateView):
    model = Finca
    template_name = 'inventory/finca_create.html'
    fields = ['descripcion','dimensionHa','ubicacion']

    def get_success_url(self):
        return reverse_lazy("finca_list") """

""" class FincaUpdateView(LoginRequiredMixin,UpdateView):
    model = Finca
    template_name = 'inventory/finca_update.html'
    fields = ['descripcion','dimensionHa','ubicacion']

    def get_success_url(self):
        return reverse_lazy("finca_list")

class FincaDeleteView(LoginRequiredMixin,DeleteView):
    model = Finca
    template_name = 'inventory/finca_delete.html'

    def get_success_url(self):
        return reverse_lazy("finca_list") """
