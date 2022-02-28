# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import include, path
from .views import  login_view
from django.contrib.auth.views import LogoutView
from apps.authentication.views import UserListView

urlpatterns = [
    path("accounts/users/", UserListView.as_view(), name="user_list"),
    path('accounts/login/', login_view, name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
]
