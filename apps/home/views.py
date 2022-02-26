# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect, reverse


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    return render(request, "home/page-blank.html", {})
