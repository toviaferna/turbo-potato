# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django_tables2 import SingleTableMixin
from apps.authentication.filters import UserFilter
from apps.authentication.tables import UserTable
from apps.mixins import SearchViewMixin
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.contrib.auth.models import User

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

class UserListView(LoginRequiredMixin, SearchViewMixin, SingleTableMixin, FilterView):
    model = User
    filterset_class = UserFilter
    table_class =  UserTable
    template_name = "generic/list.html"
    search_fields = ['first_name', 'username', 'email']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = "user_list"
        context['create_url'] = "user_list"
        context['title'] = "Usuarios"
        return context


