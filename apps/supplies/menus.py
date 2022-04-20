from menu import Menu, MenuItem
from django.shortcuts import reverse


children = (
    MenuItem(
        "Pedidos de compras",
        reverse("pedido_compra_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Ordenes de compras",
        reverse("orden_compra_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Compras",
        reverse("compra_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Notas de débito recibidas",
        reverse("nota_debito_recibida_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Notas de crédito recibidas",
        reverse("nota_credito_recibida_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Libro de compras",
        reverse("libro_compra_list"),
        icon="far fa-circle",
    ),
)

Menu.add_item("suministros", MenuItem("Suministros","#",icon='fa fa-shop',weight=6, children=children))