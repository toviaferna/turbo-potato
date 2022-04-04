from django.utils.html import format_html,escape
from django_tables2.columns.base import Column
from django.contrib.humanize.templatetags.humanize import intcomma
from django_tables2 import columns
from django_tables2.utils import AttributeDict
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

class BooleanColumn(columns.BooleanColumn):
    attrs = {
        "th":{
            "class":"text-center"
        },
        "td":{
            "class":"text-center"
        }
    }
    def render(self, value, record, bound_column):
        value = self._get_bool_value(record, value, bound_column)
        attrs = {"class": str(value).lower()}
        attrs.update(self.attrs.get("input", {}))
        checked = 'checked' if value else ''
        return format_html("<input type=checkbox style='pointer-events:none' {} {}>", AttributeDict(attrs).as_html(), checked)

    def value(self, record, value, bound_column):
        value = self._get_bool_value(record, value, bound_column)
        return 'SI' if value else 'NO'