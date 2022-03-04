# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.authentication.filters import UserFilter
from apps.authentication.tables import UserTable
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm
from core.views import CreateView, DeleteView, UpdateView, ListView
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

class UserListView(ListView):
    model = User
    filterset_class = UserFilter
    table_class =  UserTable
    search_fields = ['first_name', 'username', 'email']
    update_url =  "user_update"
    create_url = "user_add"
    delete_url = "user_delete"
    page_title = "Usuarios"

class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    list_url = 'user_list'
    page_title = 'Agregar usuario'

class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    list_url = 'user_list'
    page_title = 'Actualizar usuario'

class UserDeleteView(DeleteView): 
    model = User
    list_url = "user_list"
    page_title = "Eliminar usuario"
