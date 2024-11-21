import django_tables2 as tables
from django.contrib.auth import models

from core.tables import AccionTable


class UserTable(AccionTable):
    email = tables.Column(verbose_name="E-mail")
    full_name = tables.Column(verbose_name="Nombre completo")
    class Meta:
        model = models.User
        fields = ("full_name", "email", "document", "phone",)
