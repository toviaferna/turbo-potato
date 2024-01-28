from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.html import escape, format_html
from django_tables2 import columns
from django_tables2.columns.base import Column
from django_tables2.utils import AttributeDict


class NumericColumn(Column):

    attrs = {
        "th":{ "class":"text-right text-nowrap" },
        "td":{ "class":"text-right text-nowrap" },
        "tf":{ "class":"text-right text-nowrap" }
    }

    def render(self,value):
        return intcomma(value)



class TotalNumericColumn(NumericColumn):

    def render_footer(self, bound_column, table):
        value = 0
        for row in table.data:
            if hasattr(row, "es_vigente"):
                if row.es_vigente:
                    value = intcomma(sum(bound_column.accessor.resolve(row) for row in table.data if row.es_vigente))
            else:
                value = intcomma(sum(bound_column.accessor.resolve(row) for row in table.data))
        return value
                


class BooleanColumn(columns.BooleanColumn):
    attrs = {
        "th":{ "class":"text-center text-nowrap"},
        "td":{ "class":"text-center text-nowrap"}
    }
    
    # def render(self, value, record, bound_column):
    #     value = self._get_bool_value(record, value, bound_column)
    #     attrs = {"class": str(value).lower()}
    #     attrs.update(self.attrs.get("input", {}))
    #     checked = 'checked' if value else ''
    #     return format_html("<input type=checkbox style='pointer-events:none' {} {}>", AttributeDict(attrs).as_html(), checked)

    def value(self, record, value, bound_column):
        value = self._get_bool_value(record, value, bound_column)
        return 'SI' if value else 'NO'
