""" 
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator
from django.db import models
from core.utils import rename_img, create_thumbnail
from os import path
class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(
        'Nombre',
        max_length=30,
        null=False,
        default='',
        help_text='Ingrese su nombre.'
    )
    last_name = models.CharField(
        'Apellidos',
        max_length=150,
        null=False,
        default='',
        help_text='Ingrese sus apellidos.'
    )
    email = models.EmailField(
        'Correo Electrónico',
        error_messages={'unique': 'El correo electrónico ya existe.'},
        null=False,
        unique=True,
        help_text="Ingrese su correo electrónico."
    )
    doc_number = models.CharField(
        "Documento",
        help_text=mark_safe("Ingrese su número de documento de identidad"),
        max_length=15,
        unique=True
    )
    phone = models.CharField("Teléfono", max_length=20, help_text="Ingrese su numero de telefono o celular.")
    picture = models.ImageField(
        "Foto",
        upload_to=rename_img,
        null=True,
        blank=True,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone']

    @property
    def thumb(self):
        try:
            filepath, extension = path.splitext(self.picture.url)
            return f"{filepath}_th{extension}"
        except ValueError:
            return None

    @property
    def thumb_path(self):
        filepath, extension = path.splitext(self.picture.path)
        return f"{filepath}_th{extension}"

    def __str__(self):
        return '{0} ({1})'.format(self.get_full_name(), self.username)

    @property
    def full_name(self):
        return  self.get_full_name() """