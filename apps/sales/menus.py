from menu import Menu, MenuItem
from django.shortcuts import reverse


children = (
    MenuItem(
        "Apertura/Cierre de cajas",
        reverse("apertura_caja_list"),
        icon="far fa-circle",        
    ),
)

Menu.add_item("ventas", MenuItem("Ventas","#",icon='fa fa-solid fa-cart-shopping',weight=7, children=children))