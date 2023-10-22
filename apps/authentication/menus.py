from django.shortcuts import reverse
from menu import Menu, MenuItem

Menu.add_item(
    "usuarios",
    MenuItem("Usuarios", "#", icon="fas fa-user-group", weight=0),
)
