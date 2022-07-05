
from apps.farming.forms import (AcopioCalificacionForm, AcopioDetalleForm,
                                PlanActividadZafraDetalleForm)
from apps.farming.models import (AcopioCalificacion, AcopioDetalle,
                                 PlanActividadZafraDetalle)
from django.forms import widgets
from extra_views import InlineFormSetFactory


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

class AcopioDetalleInline(InlineFormSetFactory):
    model = AcopioDetalle
    form_class = AcopioDetalleForm
    factory_kwargs = {
        'extra':1 ,
        'widgets':{
            'finca':widgets.Select(
                attrs={
                    'wrapper_class':'col-sm-5',
                }
            ),
            'lote':widgets.Select(
                attrs={
                    'wrapper_class':'col-sm-4',
                }
            ),
            #'peso':DecimalMaskInput()
        }
    }
    fields = ['acopio', 'finca', 'lote', 'peso']

class AcopioCalificacionDetalleInline(InlineFormSetFactory):
    model = AcopioCalificacion
    form_class = AcopioCalificacionForm
    factory_kwargs = {
        'extra':1 ,
        'widgets':{
            'calificacion_agricola':widgets.Select(
                attrs={
                    'wrapper_class':'col-sm-5',
                }
            ),

        }
    }
    fields = ['acopio', 'calificacion_agricola', 'grado', 'porcentaje','peso']
