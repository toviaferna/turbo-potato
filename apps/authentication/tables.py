import email
import django_tables2 as tables
from django.contrib.auth.models import User
from core.tables import AccionTable

class UserTable(AccionTable):
    email = tables.Column(verbose_name="E-mail")
    class Meta:
        model = User
        fields = ("first_name", "email", "phone",)