from menu import Menu, MenuItem
from django.shortcuts import reverse
children = (
    MenuItem(
        "Marcas",
        reverse("marca_list"),
        icon="fas fa-tags",
    ),
)

Menu.add_item("inventario", MenuItem("Inventario","#",icon='fa fa-warehouse',weight=6, children=children))