import django_tables2 as tables
from django.contrib.auth.models import User

from core.tables import EditableTable

class UserTable(EditableTable):
    full_name = tables.Column(verbose_name="Nombres", orderable=False)
    class Meta:
        model = User
        fields = ("full_name", "email", "phone")