from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from apps.mixins import SearchViewMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import edit
from django_tables2 import SingleTableMixin
from django_tables2.export import ExportMixin
from django_filters.views import FilterView
from core.utils import get_deleted_objects
from core.tables.export import TableExport
class DeleteView(edit.DeleteView):
    error = None
    template_name = 'generic/remove.html'

    def get_success_url(self):
        return reverse_lazy(self.list_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deletable_objects, model_count, protected = get_deleted_objects([self.object])
        context['deletable_objects']=deletable_objects
        context['model_count']=dict(model_count).items()
        context['protected']=protected
        context['list_url'] = self.list_url
        context['title'] = self.page_title
        context['error'] = self.error
        return context
    
    def before_delete(self):
        pass

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            success_url = self.get_success_url()
            self.before_delete()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except Exception as e:
            self.error = e
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


class ListView(LoginRequiredMixin,SearchViewMixin,ExportMixin, SingleTableMixin, FilterView):
    paginate_by = 10
    template_name = 'generic/list.html'
    export_class = TableExport

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = None if not self.update_url else self.update_url
        context['delete_url'] = None if not  self.delete_url else self.delete_url
        context['create_url'] = None if not self.create_url else self.create_url
        context['title'] = self.page_title
        if not self.filterset_class:
            context['filter'] = None
        return context
    
class CreateView(LoginRequiredMixin, edit.CreateView):
    template_name = 'generic/edit.html'
    
    def get_success_url(self):
        return reverse_lazy(self.list_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] = None
        context['list_url'] = self.list_url
        context['title'] = self.page_title
        return context

class UpdateView(edit.UpdateView):
    template_name = 'generic/edit.html'

    def get_success_url(self):
        return reverse_lazy(self.list_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] = None
        context['list_url'] = self.list_url
        context['title'] = self.page_title
        return context

