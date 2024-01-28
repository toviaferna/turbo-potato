from django.shortcuts import reverse
from menu import Menu, MenuItem

#Menu.add_item("documentation", MenuItem("Ayuda", "#" ,icon='fas fa-help',weight=6, link_attrs={"target": "_blank"}))
Menu.add_item("ayuda", MenuItem("Ayuda", '#', icon='fa fa-circle-question', weight=6, link_attrs={"target": "_blank"}))
