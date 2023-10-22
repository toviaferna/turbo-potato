from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    MenuItem(
        "Informe de compras",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Informe de ventas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Actividades agricolas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Inventario deposito",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Libro de ventas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Libro de compras",
        "#",
        icon="far fa-circle",
    ),
)

Menu.add_item("informes", MenuItem("Informes","#",icon='fa fa-file-contract',weight=8, children=children))
