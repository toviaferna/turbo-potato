from menu import Menu, MenuItem
from django.shortcuts import reverse
children = (
    MenuItem(
        "Items",
        reverse("item_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Marcas",
        reverse("marca_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Categorias",
        reverse("categoria_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Depositos",
        reverse("deposito_list"),
        icon="far fa-circle",
    ),
    #MenuItem(
    #    "Tipos de items",
    #    reverse("tipo_item_list"),
    #    icon="fas fa-boxes-stacked",
    #),
    MenuItem(
        "Ajustes de stock",
        reverse("ajuste_stock_list"),
        icon="far fa-circle",
    ),
)

Menu.add_item("inventario", MenuItem("Inventario","#",icon='fa fa-warehouse',weight=6, children=children))