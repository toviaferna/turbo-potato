from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from menu import Menu, MenuItem



Menu.add_item("inicio", MenuItem("Inicio", reverse("home"),icon='fas fa-home', weight=0))
Menu.add_item("inicio", MenuItem("Inicio", reverse("home.views.index"),icon='fas fa-home', weight=0))