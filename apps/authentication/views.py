# -*- encoding: utf-8 -*-
import os
import subprocess
from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django_tables2 import SingleTableMixin

from apps.authentication import filters, forms, models, tables
from core import mixins, views


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

class UserListView(mixins.SuperUserRequiredMixin, views.ListView):
    model = models.User
    filterset_class = filters.UserFilter
    table_class =  tables.UserTable
    search_fields = ['first_name', 'username', 'email']
    update_url =  "user_update"
    create_url = "user_add"
    delete_url = "user_delete"
    page_title = "Usuarios"

class UserCreateView(mixins.SuperUserRequiredMixin, views.CreateView):
    model = models.User
    form_class = forms.CustomUserCreationForm
    list_url = 'user_list'
    page_title = 'Agregar usuario'

class UserUpdateView(mixins.SuperUserRequiredMixin, views.UpdateView):
    model = models.User
    form_class = forms.CustomUserChangeForm
    list_url = 'user_list'
    page_title = 'Actualizar usuario'

class UserDeleteView(mixins.SuperUserRequiredMixin, views.DeleteView): 
    model = models.User
    list_url = "user_list"
    page_title = "Eliminar usuario"


class DatabaseBackupView(mixins.SuperUserRequiredMixin, generic.TemplateView):
    template_name = 'authentication/backup_result.html'
    page_title = "Backup Base de Datos"
    success_url = reverse_lazy('database_backup_list')

    def get_backup_directory(self):
        # Usar una ruta específica en C:
        backup_dir = r"C:\backups"
        
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            
        return backup_dir

    def generate_backup_filename(self):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return os.path.join(self.get_backup_directory(), f'backup_agroatardecer_{timestamp}.sql')

    def create_backup(self):
        backup_file = self.generate_backup_filename()
        
        try:
            # Comando para realizar el backup
            command = (
                f'mysqldump -h localhost -P 3306 -u root -p1234 '
                f'turbo_potato > "{backup_file}"'
            )

            # Ejecutar el comando
            process = subprocess.run(
                command,
                shell=True,
                stderr=subprocess.PIPE,
                text=True
            )

            # Verificar si se creó el archivo y tiene contenido
            if os.path.exists(backup_file):
                file_size = os.path.getsize(backup_file)
                if file_size > 0:
                    return {
                        'success': True,
                        'file': backup_file,
                        'size': file_size / (1024 * 1024)  # Convertir a MB
                    }
                else:
                    os.remove(backup_file)  # Eliminar archivo vacío
                    return {
                        'success': False,
                        'error': 'El archivo de backup está vacío'
                    }
            else:
                return {
                    'success': False,
                    'error': 'No se pudo crear el archivo de backup'
                }

        except Exception as e:
            if os.path.exists(backup_file):
                os.remove(backup_file)  # Limpiar archivo en caso de error
            return {
                'success': False,
                'error': str(e)
            }

    def get(self, request, *args, **kwargs):
        result = self.create_backup()
        
        if result['success']:
            messages.success(
                request,
                f'Backup creado exitosamente en: {result["file"]} '
                f'(Tamaño: {result["size"]:.2f} MB)'
            )
        else:
            messages.error(request, f'Error al crear backup: {result["error"]}')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['backup_dir'] = self.get_backup_directory()
        return context

class BackupListView(mixins.SuperUserRequiredMixin, SingleTableMixin,  generic.ListView):
    template_name = 'authentication/backup_list.html'
    page_title = "Lista de Backups"
    context_object_name = 'backups'
    table_class = tables.BackupTable
    paginate_by = 10

    def get_queryset(self):
        backup_dir = r"C:\backups"
        if not os.path.exists(backup_dir):
            return []
            
        backups = []
        for file in os.listdir(backup_dir):
            if file.endswith('.sql'):
                path = os.path.join(backup_dir, file)
                stats = os.stat(path)
                backups.append({
                    'name': file,
                    'size': f"{stats.st_size / 1024:.2f} KB",
                    'date': datetime.fromtimestamp(stats.st_mtime)
                })
        return sorted(backups, key=lambda x: x['date'], reverse=True)