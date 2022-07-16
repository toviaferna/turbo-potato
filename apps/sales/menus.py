from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    MenuItem(
        "Apertura/Cierre de cajas",
        reverse("apertura_caja_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Arqueos",
        reverse("arqueo_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Transferencia de cuentas",
        reverse("transferencia_cuenta_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Ventas",
        reverse("venta_list"),
        icon="far fa-circle",        
    ),
)

Menu.add_item("ventas", MenuItem("Ventas","#",icon='fa fa-cart-shopping',weight=7, children=children))
