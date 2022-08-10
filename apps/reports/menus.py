from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    MenuItem(
        "Informe de compras",
        reverse("informe_compra_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Informe de ventas",
        reverse("informe_venta_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Actividades agricolas",
        reverse("informe_actividad_agricola_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Inventario deposito",
        reverse("informe_inventario_deposito_list"),
        icon="far fa-circle",
    ),
)

Menu.add_item("informes", MenuItem("Informes","#",icon='fa fa-file-contract',weight=8, children=children))
