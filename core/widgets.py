from django import forms
from calculation import widgets

class DateInput(forms.DateInput):
    input_type = 'date'
    def __init__(self, attrs=None, format=None):
        super().__init__(attrs, format='%Y-%m-%d' if format is None else format)


class SumInput(widgets.SumInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {
            'readonly':True, 
            'class':'text-danger text-right bg-white border-0 p-0' 
        }
        super().__init__(*args, **kwargs)