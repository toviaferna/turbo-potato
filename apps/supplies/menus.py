from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    MenuItem(
        "Pedidos de compras",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Ordenes de compras",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Compras",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Notas de débito recibidas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Notas de crédito recibidas",
        "#",
        icon="far fa-circle",
    ),
)

Menu.add_item(
    "suministros",
    MenuItem("Suministros", "#", icon="fa fa-shop", weight=6, children=children),
)
