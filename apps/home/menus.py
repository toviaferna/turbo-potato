from menu import Menu, MenuItem
from django.shortcuts import reverse



Menu.add_item("inicio", MenuItem("Inicio", reverse("home"),icon='fas fa-home',weight=6))
