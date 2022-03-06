from menu import Menu, MenuItem
from django.shortcuts import reverse
children = (
    MenuItem(
        "Items",
        reverse("item_list"),
        icon="fas fa-qrcode",
    ),
    MenuItem(
        "Marcas",
        reverse("marca_list"),
        icon="fas fa-tags",
    ),
    MenuItem(
        "Categorias",
        reverse("categoria_list"),
        icon="fas fa-chart-gantt",
    ),
    MenuItem(
        "Depositos",
        reverse("deposito_list"),
        icon="fas fa-cart-flatbed",
    ),
    MenuItem(
        "Tipos de items",
        reverse("tipo_item_list"),
        icon="fas fa-boxes-stacked",
    ),
)

Menu.add_item("inventario", MenuItem("Inventario","#",icon='fa fa-warehouse',weight=6, children=children))