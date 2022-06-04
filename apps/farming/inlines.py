
from extra_views import InlineFormSetFactory
from apps.farming.models import PlanActividadZafraDetalle
from apps.farming.forms import PlanActividadZafraDetalleForm
from django.forms import widgets

class PlanActividadZafraDetalleInline(InlineFormSetFactory):
    model = PlanActividadZafraDetalle
    form_class = PlanActividadZafraDetalleForm
    factory_kwargs = {
        'extra':1 ,
        'widgets':{
            'fecha_actividad':widgets.DateInput(
                attrs={
                    'wrapper_class':'col-sm-1',
                    'type':'date'
                }
            ),
            'finca':widgets.Select(
                attrs={
                    'wrapper_class':'col-sm-2',
                }
            ),
            'tipo_actividad_agricola':widgets.Select(
                attrs={
                    'wrapper_class':'col-sm-2',
                }
            ),
            'costo':widgets.NumberInput(
                attrs={
                    'wrapper_class':'col-sm-2',
                }
            ),

        }
    }
    fields =  ['fecha_actividad', 'finca', 'tipo_actividad_agricola','descripcion','costo']
