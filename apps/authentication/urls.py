# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import include, path
from .views import  login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', login_view, name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
]
