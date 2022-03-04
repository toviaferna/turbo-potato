from apps.mixins import SearchViewMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import list
from django.views.generic.edit import DeleteView
from django_tables2 import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django_filters.views import FilterView


class CustomDeleteView(DeleteView):
    error = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

def get_deleted_objects(objs):
    """
    get related objects to delete
    """
    collector = NestedObjects(using='default')
    collector.collect(objs)

    def format_callback(obj):
        opts = obj._meta
        no_edit_link = '%s: %s' % (capfirst(opts.verbose_name),
                                   force_text(obj))
        return no_edit_link

    to_delete = collector.nested(format_callback)
    protected = [format_callback(obj) for obj in collector.protected]
    model_count = {model._meta.verbose_name_plural: len(
        objs) for model, objs in collector.model_objs.items()}
    return to_delete, model_count, protected


class ListView(LoginRequiredMixin,SearchViewMixin,ExportMixin, SingleTableMixin, FilterView):
    paginate_by = 10
    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = self.update_url
        context['delete_url'] = self.delete_url
        context['create_url'] = self.create_url
        context['title'] = self.page_title
        if not self.filterset_class:
            context['filter'] = None
        return context