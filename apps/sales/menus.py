from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    MenuItem(
        "Apertura/Cierre de cajas",
        "#",
        icon="far fa-circle",        
    ),
    MenuItem(
        "Arqueos",
        "#",
        icon="far fa-circle",        
    ),
    MenuItem(
        "Transferencia de cuentas",
        "#",
        icon="far fa-circle",        
    ),
    MenuItem(
        "Ventas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Notas de débito emitidas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Notas de crédito emitidas",
        "#",
        icon="far fa-circle",
    ),
    MenuItem(
        "Cobros",
        "#",
        icon="far fa-circle",
    ),

)

Menu.add_item("ventas", MenuItem("Ventas","#",icon='fa fa-cart-shopping',weight=7, children=children))
