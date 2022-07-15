import django_tables2 as tables
from core.tables import AccionTable
from django.contrib.auth import models


class UserTable(AccionTable):
    email = tables.Column(verbose_name="E-mail")
    class Meta:
        model = models.User
        fields = ("first_name", "email", "phone",)
