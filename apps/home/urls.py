# -*- encoding: utf-8 -*-
from apps.home import views
from django.conf.urls import url
from django.urls import path, re_path

urlpatterns = [

   url(r"^$", views.index, name="home"),

]
