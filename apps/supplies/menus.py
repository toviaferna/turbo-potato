from menu import Menu, MenuItem
from django.shortcuts import reverse
children = (
    MenuItem(
        "Marcas",
        reverse("marca_list"),
        icon="fas fa-tags",
    ),
)

Menu.add_item("suministro", MenuItem("Suministro","#",icon='fas fa-store-alt',weight=6, children=children))