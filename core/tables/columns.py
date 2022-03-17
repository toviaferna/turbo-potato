
from django.utils.html import format_html
from django_tables2.columns.base import Column
from django.contrib.humanize.templatetags.humanize import intcomma

class NumberColumn(Column):
    attrs = {
        "th":{ "class":"text-right" },
        "td":{ "class":"text-right" },
        "tf":{ "class":"text-right" }
    }
    
    def render(self,value):
        return intcomma(value)
    
    def render_footer(self, bound_column, table):
        return "Total: "+intcomma(sum(bound_column.accessor.resolve(row) for row in table.data if row.es_vigente))

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