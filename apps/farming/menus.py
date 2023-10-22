from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    MenuItem(
        "Fincas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Calificaciones Agrícolas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Tipos de Actividades Agrícolas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Tipos de Maquinarias Agrícolas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Maquinarias Agrícolas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Zafras",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Lotes",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Plan de actividades por zafra",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Contratos",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Acopios",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Actividades Agricolas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Liquidaciones Agricolas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Cierres de zafras",
        "#",
        icon="far fa-circle",
    ),
)

Menu.add_item(
    "agricultura",
    MenuItem("Agricultura", "#", icon="fa fa-tractor", weight=6, children=children),
)
