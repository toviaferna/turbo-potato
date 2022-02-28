from django.template.loader import render_to_string
from crispy_forms.layout import TemplateNameMixin
from crispy_forms.utils import TEMPLATE_PACK, flatatt

class BaseButton(TemplateNameMixin):
    def __init__(self, **kwargs):
        if not getattr(self, 'field_classes'):
            self.field_classes = ""
        self.id = kwargs.pop("css_id", "")
        self.attrs = {}

        if "css_class" in kwargs:
            self.field_classes += " %s" % kwargs.pop("css_class")

        self.flat_attrs = flatatt(kwargs)


class CancelButton(BaseButton):
    
    def __init__(self, **kwargs):
        self.field_classes = "btn btn-secondary"
        super().__init__(**kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        context.update({"cancel_button": self})
        return render_to_string('includes/cancel_button.html', context.flatten())