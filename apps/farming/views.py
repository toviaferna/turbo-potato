from django.shortcuts import render
from django.urls import reverse_lazy
from django_tables2 import SingleTableMixin
from apps.farming.forms import FincaForm
from apps.farming.tables import FincaTable
from .models import Finca
from apps.mixins import SearchViewMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from core.utils import get_deleted_objects

# FINCA
class FincaListView(LoginRequiredMixin,SearchViewMixin, SingleTableMixin, ListView):
    model = Finca
    table_class = FincaTable
    paginate_by = 6
    search_fields = ['descripcion','ubicacion']
    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'finca_update'
        context['delete_url'] = 'finca_delete'
        context['create_url'] = 'finca_create'
        context['title'] = "Fincas"
        return context

class FincaCreateView(LoginRequiredMixin,CreateView):
    form_class = FincaForm
    model = Finca
    template_name = 'generic/edit.html'

    def get_success_url(self):
        return reverse_lazy("finca_list") 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] = None
        context['list_url'] = 'finca_list'
        context['title'] = "Agregar fincas"
        return context

class FincaUpdateView(LoginRequiredMixin,UpdateView):
    form_class = FincaForm
    model = Finca
    template_name = 'generic/edit.html'

    def get_success_url(self):
        return reverse_lazy("finca_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] = None
        context['list_url'] = 'finca_list'
        context['title'] = "Editar fincas"
        return context

class FincaDeleteView(LoginRequiredMixin,DeleteView):
    model = Finca
    template_name = 'generic/remove.html'

    def get_success_url(self):
        return reverse_lazy("finca_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = 'finca_list'
        deletable_objects, model_count, protected = get_deleted_objects([self.object])
        context['deletable_objects']=deletable_objects
        context['model_count']=dict(model_count).items()
        context['protected']=protected
        context['title'] = "Eliminar fincas"
        return context
