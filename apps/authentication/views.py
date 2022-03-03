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
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from core.views import CustomDeleteView, ListView
from django.urls import reverse_lazy
from core.utils import get_deleted_objects

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

class UserListView(ListView):
    model = User
    filterset_class = UserFilter
    table_class =  UserTable
    template_name = "generic/list.html"
    search_fields = ['first_name', 'username', 'email']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = "user_update"
        context['delete_url'] = "user_delete"
        context['create_url'] = "user_add"
        context['title'] = "Usuarios"
        return context


class UserCreateView(LoginRequiredMixin, CreateView):

    model = User
    form_class = CustomUserCreationForm
    template_name = 'generic/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] = None
        context['title'] = "Agregar Usuario"
        context['list_url'] = 'user_list'
        return context

    def get_success_url(self):
        return reverse_lazy('user_list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'generic/edit.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] =  None
        context['list_url'] = 'user_list'
        context['title'] = 'Actualizar usuario'
        return context

    def get_success_url(self):
        return reverse_lazy("user_list")

class UserDeleteView(LoginRequiredMixin, CustomDeleteView): 
    model = User
    template_name = "generic/remove.html"
    success_url = "user_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = 'user_list'
        deletable_objects, model_count, protected = get_deleted_objects([self.object])
        context['deletable_objects']=deletable_objects
        context['model_count']=dict(model_count).items()
        context['protected']=protected
        context['title'] = "Eliminar usuario"
        return context

    def get_success_url(self):
        return reverse_lazy("user_list")