# -*- encoding: utf-8 -*-
from apps.authentication import filters, forms, models, tables
from core import views
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def login_view(request):
    form = forms.LoginForm(request.POST or None)
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
                msg = 'Datos no validos.'
        else:
            msg = 'Error al validar el formulario'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

class UserListView(views.ListView):
    model = models.User
    filterset_class = filters.UserFilter
    table_class =  tables.UserTable
    search_fields = ['first_name', 'username', 'email']
    update_url =  "user_update"
    create_url = "user_add"
    delete_url = "user_delete"
    page_title = "Usuarios"

class UserCreateView(views.CreateView):
    model = models.User
    form_class = forms.CustomUserCreationForm
    list_url = 'user_list'
    page_title = 'Agregar usuario'

class UserUpdateView(views.UpdateView):
    model = models.User
    form_class = forms.CustomUserChangeForm
    list_url = 'user_list'
    page_title = 'Actualizar usuario'

class UserDeleteView(views.DeleteView): 
    model = models.User
    list_url = "user_list"
    page_title = "Eliminar usuario"


