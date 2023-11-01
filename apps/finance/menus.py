from django.shortcuts import reverse
from menu import Menu, MenuItem

referencial = (
    MenuItem(
        "Bancos",
        reverse("banco_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Paises",
        reverse("pais_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Departamentos",
        reverse("departamento_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Distrito",
        reverse("distrito_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Localidad",
        reverse("localidad_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Tipos de impuesto",
        reverse("impuesto_list"),
        icon="far fa-circle",
    ),
)

children = (
    MenuItem(
        "Personas",
        reverse("persona_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Cuentas",
        reverse("cuenta_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Referenciales",
        "#",
        icon="far fa-circle",
        children=referencial
    ),
)

Menu.add_item("finanzas", MenuItem("Finanzas","#",icon='fa fa-coins',weight=6, children=children))