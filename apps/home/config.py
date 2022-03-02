# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'apps.home'
    label = 'apps_home'
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = 'Inicio'
