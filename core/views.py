from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.forms import widgets
from django.forms.formsets import all_valid
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, detail, edit
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from core.mixins import (FormsetInlinesMetaMixin, SearchViewMixin,
                         SelectionMixin)
from core.tables.export import TableExport
from core.tables.mixins import ExportMixin
from core.utils import get_deleted_objects


class DeleteView(LoginRequiredMixin, edit.DeleteView, metaclass=widgets.MediaDefiningClass):
    error = None
    template_name = 'generic/remove.html'
    page_title = None
    page_subtitle = None

    def get_success_url(self):
        return reverse_lazy(self.list_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deletable_objects, model_count, protected = get_deleted_objects([self.object])
        context['deletable_objects']=deletable_objects
        context['model_count']=dict(model_count).items()
        context['protected']=protected
        context['list_url'] = self.list_url
        context['title'] = "Eliminar "+self.model._meta.verbose_name.title() if self.page_title is None else self.page_title
        context['subtitle'] = f"Desea eliminar: {self.object}?" if self.page_subtitle is None else self.page_subtitle
        context['error'] = self.error
        context['delete_button_text'] = "Eliminar"
        context['media'] = self.media
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

class AnnulledView(DeleteView):
    mensaje_anulado = "Ya fue anulado!"
    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        success_url = self.get_success_url()
        try:
            self.object = self.get_object()
            if self.object.es_vigente == False:
                raise Exception(self.mensaje_anulado)
            else:
                self.object.es_vigente = False
                self.object.save()
        except  Exception as e:
            self.error = e
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        return HttpResponseRedirect(success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deletable_objects, model_count, protected = get_deleted_objects([self.object])
        context['deletable_objects']=deletable_objects
        context['model_count']=dict(model_count).items()
        context['protected']=protected
        context['list_url'] = self.list_url
        context['title'] = "Anular "+self.model._meta.verbose_name.title() if self.page_title is None else self.page_title
        context['subtitle'] = f"Desea anular: {str(self.object)} ?" if self.page_subtitle is None else self.page_subtitle
        context['error'] = self.error
        return context

class ListView(LoginRequiredMixin,SearchViewMixin, ExportMixin, SingleTableMixin, FilterView):
    paginate_by = 10
    template_name = 'generic/list.html'
    export_class = TableExport
    page_title = None
    export_page_orientation = "portrait"
    download_url = None
    update_url = None
    delete_url = None
    create_url = None
    export_button = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = None if not self.update_url else self.update_url
        context['delete_url'] = None if not  self.delete_url else self.delete_url
        context['create_url'] = None if not self.create_url else self.create_url
        context['download_url'] = None if not self.download_url else self.download_url
        context['title'] = "Listado de "+self.model._meta.verbose_name_plural.title() if self.page_title is None else self.page_title
        context['export_button'] = self.export_button
        if not self.filterset_class:
            context['filter'] = None
        return context


class CreateView(LoginRequiredMixin, FormsetInlinesMetaMixin, CreateWithInlinesView, metaclass=widgets.MediaDefiningClass):
    template_name = 'generic/edit.html'
    page_title = None

    def get_success_url(self):
        return reverse_lazy(self.list_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] = None
        context['list_url'] = self.list_url
        context['title'] = context['title'] = "Agregar "+self.model._meta.verbose_name.lower() if self.page_title is None else self.page_title
        context['media'] = self.media


        return context

    def run_form_extra_validation(self, form, inlines):
        """ ejecutar validaciones adicionales de formularios """

    def run_form_extra_validation_form_master(self, form):
        """ ejecutar validaciones adicionales de formularios """
        return True

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

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

class UpdateView(LoginRequiredMixin, FormsetInlinesMetaMixin, UpdateWithInlinesView, metaclass=widgets.MediaDefiningClass):
    template_name = 'generic/edit.html'
    page_title = None

    def get_success_url(self):
        return reverse_lazy(self.list_url)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] = None
        context['list_url'] = self.list_url
        context['title'] = "Modificar "+self.model._meta.verbose_name.lower() if self.page_title is None else self.page_title
        context['media'] = self.media
        return context

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

class DetailView(LoginRequiredMixin, detail.DetailView, metaclass=widgets.MediaDefiningClass):
    template_name = 'generic/detail.html'
    page_title = None

    def get_object_data(self):
        for field in self.object._meta.fields:
            if isinstance(field, models.AutoField):
                continue
            elif field.auto_created:
                continue
            else:
                choice_display_attr = "get_{}_display".format(field.name)
            if hasattr(self.object, choice_display_attr):
                value = getattr(self.object, choice_display_attr)()
            else:
                value = getattr(self.object, field.name)

            if value is not None:
                yield (field.verbose_name.title(), value)
                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_data'] = self.get_object_data()
        context['helper'] = None
        context['list_url'] = self.list_url
        context['title'] = "Detalles de "+self.model._meta.verbose_name.lower() if self.page_title is None else self.page_title
        context['media'] = self.media
        return context

class SelectionListView(SelectionMixin, ListView):
    """ Vista de seleccion de tipo listado """


class SelectionFormView(LoginRequiredMixin, SelectionMixin, FormView, metaclass=widgets.MediaDefiningClass):
    page_title = None
    selection_title = None
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] = None
        context['list_url'] = self.list_url
        context['selection_title'] = self.selection_title
        context['title'] = context['title'] = "Agregar "+self.model._meta.verbose_name.lower() if self.page_title is None else self.page_title
        context['media'] = self.media
        return context

