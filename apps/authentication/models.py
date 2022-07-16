from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    document = models.CharField(
        "Documento",
        help_text="Ingrese su número de documento de identidad",
        max_length=15,
        unique=True,
    )
    phone = models.CharField(
        "Teléfono", max_length=20, help_text="Ingrese su numero de telefono o celular."
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "phone"]

    def __str__(self):
        return "{0} ({1})".format(self.get_full_name(), self.username)

    @property
    def full_name(self):
        return self.get_full_name()
