from menu import Menu, MenuItem
from django.shortcuts import reverse



Menu.add_item("usuarios", MenuItem("Usuarios", reverse("user_list"),icon='fas fa-users',weight=6))
