# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home.views import index
from django.conf.urls import url

urlpatterns = [

   url(r"^$", index, name="home"),

]
