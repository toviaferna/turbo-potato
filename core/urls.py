# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls import url

urlpatterns = [         # Django admin route
    path("", include("apps.authentication.urls")),
    path("farming/", include("apps.farming.urls")),             # UI Kits Html files
    path("", include("apps.home.urls")),             # UI Kits Html files
]
