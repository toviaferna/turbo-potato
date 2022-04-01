

from django.forms.models import ModelForm
from core.layouts import CancelButton
from .models import Finca
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder,Layout, Submit

class FincaForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "dimension_ha",
            "ubicacion",
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),               
        )
    class Meta:
        model = Finca
        fields = ['descripcion','dimension_ha','ubicacion']