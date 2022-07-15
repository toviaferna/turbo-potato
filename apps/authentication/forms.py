# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.authentication import models
from core.layouts import CancelButton, SaveButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Layout, Row
from django.contrib.auth import forms
from django.forms import CharField, Form, PasswordInput, TextInput


class LoginForm(Form):
    username = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Nombre de usuario.",
                "class": "form-control"
            }
        ))
    password = CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": "Contraseña.",
                "class": "form-control"
            }
        ))

class CustomUserCreationForm(forms.UserCreationForm):
    """
    Custom user register form
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Row(
                Column('first_name'),
                Column('last_name'),
            ),
            Row(
                Column('username'),
                Column('email'),
            ),
            Row(
                Column('password1'),
                Column('password2'), 
            ),
            "is_active",
            ButtonHolder(
                SaveButton(),
                CancelButton()
            )
        )
    class Meta(forms.UserCreationForm.Meta):
        model = models.User
        fields = forms.UserCreationForm.Meta.fields + ("first_name", "last_name", "email","is_active",)

class CustomUserChangeForm(forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        #self.fields['password'].help_text = "Las contraseñas no se almacenan en bruto, así que no hay manera de ver la contraseña del usuario, pero se puede cambiar la contraseña mediante <a href='%s'>este formulario.</a>"%reverse("password_change")
        self.helper.layout = Layout(
            Row(
                Column('first_name'),
                Column('last_name'),
            ),
            Row(
                Column('username'),
                Column('email'),
            ),
            Row(
                Column('password'),
                Column()
            ),
            "is_active",
            ButtonHolder(
                SaveButton(),
                CancelButton(),
            )
        )
    class Meta(forms.UserCreationForm.Meta):
        model = models.User
        fields = forms.UserCreationForm.Meta.fields + ("first_name", "last_name", "email","is_active",)

