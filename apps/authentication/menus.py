from django.shortcuts import reverse
from menu import Menu, MenuItem


def is_superuser(request):
    return request.user.is_superuser

Menu.add_item(
    "usuarios",
    MenuItem(
        "Usuarios", 
        reverse("user_list"), 
        icon="fas fa-user-group", 
        weight=0,
        check=is_superuser
    ),
)

Menu.add_item(
    "backup",
    MenuItem(
        "Copias de Seguridad", 
        reverse("database_backup_list"), 
        icon="fas fa-shield", 
        weight=0,
        check=is_superuser
    ),
)
