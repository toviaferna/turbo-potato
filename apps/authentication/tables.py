import django_tables2 as tables
from django.contrib.auth.models import User

from core.tables import BaseTable

class UserTable(BaseTable):
    full_name = tables.Column(verbose_name="Nombres", orderable=False)
    class Meta:
        model = User
        fields = ("full_name", "email", "phone")