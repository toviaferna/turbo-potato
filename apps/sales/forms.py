


from core.layouts import CancelButton, SaveButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Layout, Row, Submit
from django.forms import ModelForm

from .models import AperturaCaja


class AperturaCajaCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "empleado",
            "observacion",
            "monto_inicio",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = AperturaCaja
        fields = ["empleado","observacion","monto_inicio",]

