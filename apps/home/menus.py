from django.core.urlresolvers import reverse
from menu import Menu, MenuItem




Menu.add_item("inicio", MenuItem("Inicio", reverse("home.views.index"),icon='fas fa-home', weight=0))

