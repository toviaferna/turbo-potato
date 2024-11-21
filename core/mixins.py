import json

from dal_select2 import widgets
from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import FieldDoesNotExist, PermissionDenied
from django.db.models import Q
from django.shortcuts import redirect


class SearchViewMixin:
    search_fields = None

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_fields:
            or_condition = Q()
            value = self.get_search_query()
            if value:
                for field in self.search_fields:
                    or_condition.add(Q(**{f"{field}__icontains": value}), Q.OR)
                queryset = queryset.filter(or_condition)

        return queryset

    def get_search_query(self):
        return self.request.GET.get("q", None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.get_search_query()
        context["search_placeholder"] = self.get_search_placeholder()
        # agregar bandera para ocultara en generic list
        context["search"] = True
        return context

    def _get_model_name_by_lookup(self, lookup):
        model = self.model
        for name in lookup.split("__"):
            try:
                field = model._meta.get_field(name)
            except FieldDoesNotExist:
                # name is probably a lookup or transform such as __contains
                break
            if hasattr(field, "related_model"):
                # field is a relation
                if field.related_model:
                    model = field.related_model

            else:
                # field is not a relation, any name that follows is
                # probably a lookup or transform
                break
        return model

    def get_search_placeholder(self):
        placeholder = ""
        labels = []
        model = self.model
        for field in self.search_fields:
            if len(field.split("__")) == 1:
                labels.append(model._meta.get_field(field).verbose_name)
            else:
                related = self._get_model_name_by_lookup(field)
                model_name = related._meta.verbose_name
                try:
                    field_name = field.split("__")[-1:][0]
                    label = related._meta.get_field(field_name).verbose_name
                    labels.append(f"{model_name}: {label}")
                except FieldDoesNotExist:
                    pass
        if labels:
            placeholder = ", ".join(map(str.capitalize, map(str, labels)))
        return placeholder


class SelectionMixin:
    selection_title = None
    next_url = None
    back_url = None
    template_name = "generic/selection.html"
    params_name = "selection-pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selection_title"] = self.selection_title
        context["next_url"] = None if not self.next_url else self.next_url
        context["back_url"] = None if not self.back_url else self.back_url
        context["params_name"] = self.params_name
        return context


class FormsetInlinesMetaMixin(object):
    _formset_inlines_meta = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.build_formset_inlines_meta()

    def build_formset_inlines_meta(self):
        if not hasattr(self, "inlines"):
            return None

        for i, formset_class in enumerate(self.inlines):
            self._formset_inlines_meta[formset_class.__name__] = {"index": i}

    def get_formset_inlines_meta(self):
        return self._formset_inlines_meta

    def get_context_data(self, **kwargs):
        """
        get and update context data
        """
        context = super().get_context_data(**kwargs)
        context["formset_inlines_meta"] = self.get_formset_inlines_meta()
        return context


class MaskInputMixin:
    mask = {}

    class Media:
        js = [
            "assets/js/mask.js",
            "https://cdnjs.cloudflare.com/ajax/libs/jquery.inputmask/5.0.7/inputmask.js",
        ]

    def __init__(self, *args, **kwargs):
        mask = kwargs.pop("mask", None)
        attrs = kwargs.get("attrs", {})
        if attrs is None:
            attrs = {}
        kwargs["attrs"] = attrs
        super().__init__(*args, **kwargs)
        if mask:
            self.mask.update(mask)

    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs["data-inputmask"] = (
            json.dumps(self.mask).replace("{", "").replace("}", "")
        )
        rendered = super().render(name, value, attrs=attrs, renderer=None)
        return rendered

    def format_value(self, value):
        """
        Return a value as it should appear when rendered in a template.
        """
        if value == "" or value is None:
            return None
        return str(value)


class Select2WidgetMixin(widgets.Select2WidgetMixin):
    @property
    def media(self):
        """Return JS/CSS resources for the widget."""
        extra = "" if settings.DEBUG else ".min"
        i18n_name = self._get_language_code()
        i18n_file = ("%s%s.js" % (widgets.I18N_PATH, i18n_name),) if i18n_name else ()

        return forms.Media(
            js=(
                "admin/js/vendor/select2/select2.full.js",
                "autocomplete_light/autocomplete_light%s.js" % extra,
                "autocomplete_light/select2%s.js" % extra,
                "assets/js/select2/select2.js"
            )
            + i18n_file,
            css={
                "screen": (
                    "admin/css/vendor/select2/select2%s.css" % extra,
                    "admin/css/autocomplete.css",
                    "autocomplete_light/select2.css",
                    "assets/css/select2/select2-bootstrap4.css",
                ),
            },
        )

class SuperUserRequiredMixin(UserPassesTestMixin):
   
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().handle_no_permission()