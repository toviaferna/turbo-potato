from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    MenuItem(
        "Personas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Cuentas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Bancos",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Paises",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Departamentos",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Distrito",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Localidad",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Tipos de impuesto",
        "#",
        icon="far fa-circle",
    ),
)

Menu.add_item("finanzas", MenuItem("Finanzas","#",icon='fa fa-coins',weight=6, children=children))