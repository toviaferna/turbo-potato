from menu import Menu, MenuItem
from django.shortcuts import reverse
children = (
    MenuItem(
        "Personas",
        reverse("persona_list"),
        #icon="fa fa-users",
    ),
    MenuItem(
        "Cuentas",
        reverse("cuenta_list"),
        #icon="fa fa-money-check-dollar",
    ),
    MenuItem(
        "Bancos",
        reverse("banco_list"),
        #icon="fas fa-building-columns",
    ),
    MenuItem(
        "Paises",
        reverse("pais_list"),
        #icon="fa fa-flag",
    ),
    MenuItem(
        "Departamentos",
        reverse("departamento_list"),
        #icon="fa fa-regular fa-flag",
    ),
    MenuItem(
        "Distrito",
        reverse("distrito_list"),
        #icon="fa fa-flag-checkered",
    ),
    MenuItem(
        "Localidad",
        reverse("localidad_list"),
        #icon="fa fa-sign-hanging",
    ),
    MenuItem(
        "Tipos de impuesto",
        reverse("impuesto_list"),
        #icon="fas fa-percent",
    ),
)

Menu.add_item("finanzas", MenuItem("Finanzas","#",icon='fa fa-coins',weight=6, children=children))