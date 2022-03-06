from django.forms.models import ModelForm
from core.layouts import CancelButton
from .models import Categoria, Deposito, Item, Marca, TipoItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder,Layout, Submit, Row, Column

class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = Marca
        fields = ['descripcion',]

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = Categoria
        fields = ['descripcion',]

class TipoItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = TipoItem
        fields = ['descripcion',]

class ItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("descripcion"),
                Column("codigo_barra"),
                Column("tipo_item"),
            ),
            Row(
                Column("categoria"),
                Column("marca"),
                Column("tipo_impuesto"),
            ),
            Row(
                Column("precio"),
                Column("es_activo"),
            ),
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = Item
        fields = ['descripcion','codigo_barra','tipo_item','categoria','marca','tipo_impuesto','precio','es_activo']

class DepositoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "descripcion",
            "es_planta_acopiadora",
            ButtonHolder(
                Submit("submit", "Guardar", css_class="btn btn-primary"),
                CancelButton(),
            ),
        )
    class Meta:
        model = Deposito
        fields = ['descripcion','es_planta_acopiadora']