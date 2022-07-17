# -*- encoding: utf-8 -*-


from apps.authentication import models
from core.layouts import CancelButton, FormActions, SaveButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Layout, Row
from django.contrib.auth import forms
from django.forms import CharField, Form, PasswordInput, TextInput


class LoginForm(Form):
    username = CharField(
        widget=TextInput(
            attrs={"placeholder": "Nombre de usuario.", "class": "form-control"}
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={"placeholder": "Contraseña.", "class": "form-control"}
        )
    )


class CustomUserCreationForm(forms.UserCreationForm):
    """
    Custom user register form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["autofocus"] = True
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Row(Column("first_name"), Column("last_name"), Column("document")),
            Row(
                Column("username"),
                Column("email"),
                Column("phone"),
            ),
            Row(Column("password1"), Column("password2"), Column()),
            "is_active",
            FormActions()
        )

    class Meta(forms.UserCreationForm.Meta):
        model = models.User
        fields = forms.UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "is_active",
            "document",
            "phone",
        )
        labels = {"first_name": "Nombres"}


class CustomUserChangeForm(forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields[
            "password"
        ].help_text = "Las contraseñas no se almacenan en bruto, así que no hay manera de ver la contraseña del usuario."
        self.helper.layout = Layout(
            Row(
                Column("first_name", help_text="help_text="),
                Column("last_name"),
                Column("document"),
            ),
            Row(
                Column("username"),
                Column("email"),
                Column("phone"),
            ),
            Row(Column("password"), Column(), Column()),
            "is_active",
            FormActions()
        )

    class Meta(forms.UserCreationForm.Meta):
        model = models.User
        fields = forms.UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "is_active",
            "document",
            "phone",
        )
        labels = {"first_name": "Nombres"}
        # help_texts = {
        #    "first_name":""
        # }
