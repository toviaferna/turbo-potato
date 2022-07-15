# -*- encoding: utf-8 -*-
from apps.authentication import filters, forms, models, tables
from core import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


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

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('password_change_done_')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cambiar contraseña"
        return context

class PasswordChangeDoneView(TemplateView):
    template_name = 'accounts/password_change_done.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cambio de contraseña exitoso"
        return context
