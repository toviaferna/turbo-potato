
from django.utils.html import format_html
from django_tables2.columns.base import Column


class BooleanColumn(Column):
    attrs = {
        "th":{
            "class":"text-center"
        },
        "td":{
            "class":"text-center"
        }
    }

    def render(self, value):
        if value:
            value = 'checked'
        return format_html('<input type=checkbox style="pointer-events:none" {}>',value)