from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    MenuItem(
        "Items",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Marcas",
        reverse("marca_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Categorias",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Depositos",
        "#",
        icon="far fa-circle",
    ),
    #MenuItem(
    #    "Tipos de items",
    #    reverse("tipo_item_list"),
    #    icon="fas fa-boxes-stacked",
    #),
    MenuItem(
        "Ajustes de stock",
        "#",
        icon="far fa-circle",
    ),
)

Menu.add_item("inventario", MenuItem("Inventario","#",icon='fa fa-warehouse',weight=6, children=children))