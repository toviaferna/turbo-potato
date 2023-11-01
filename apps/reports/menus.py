from django.shortcuts import reverse
from menu import Menu, MenuItem

compra = (
    MenuItem(
        "Informe de compras",
        reverse("informe_compra_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Libro de compras",
        reverse("libro_compra_list"),
        icon="far fa-circle",
    ),
)

venta = (
    MenuItem(
        "Informe de ventas",
        reverse("informe_venta_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Libro de ventas",
        reverse("libro_venta_list"),
        icon="far fa-circle",
    ),
)

agricultura = (
    MenuItem(
        "Actividades agricolas",
        reverse("informe_actividad_agricola_list"),
        icon="far fa-circle",
    ),
)

inventario = (
    MenuItem(
        "Inventario deposito",
        reverse("informe_inventario_deposito_list"),
        icon="far fa-circle",
    ),
)

children = (
    MenuItem(
        "Compras",
        "#",
        icon="far fa-circle",
        children=compra
    ),
    MenuItem(
        "Ventas",
        "#",
        icon="far fa-circle",
        children=venta
    ),
    MenuItem(
        "Agricultura",
        "#",
        icon="far fa-circle",
        children=agricultura
    ),
    MenuItem(
        "Inventario",
        "#",
        icon="far fa-circle",
        children=inventario
    ),
)

Menu.add_item("informes", MenuItem("Informes","#",icon='fa fa-file-contract',weight=8, children=children))
