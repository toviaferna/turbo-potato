


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
            Row(
                Column("empleado"),
                Column("monto_inicio", css_class="col-sm-3"),
                
            ),
            Row(
               Column("observacion",),
            ),
            
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            ),
        )
    class Meta:
        model = AperturaCaja
        fields = ["empleado","observacion","monto_inicio",]

