from menu import Menu, MenuItem
from django.shortcuts import reverse


children = (
    MenuItem(
        "Pedidos de compras",
        reverse("pedido_compra_list"),
        icon="fa fa-cart-plus",        
    ),
    MenuItem(
        "Ordenes de compras",
        reverse("orden_compra_list"),
        icon="fa fa-list",        
    ),
)

Menu.add_item("suministros", MenuItem("Suministros","#",icon='fa fa-shop',weight=6, children=children))