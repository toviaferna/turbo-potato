from django.shortcuts import reverse
from menu import Menu, MenuItem

referencial = (
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
    MenuItem(
        "Unidad de Medida",
        reverse("unidad_medida_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Tipos de items",
        reverse("tipo_item_list"),
        icon="far fa-circle",
    ),
)

children = (
    MenuItem(
        "Items",
        reverse("item_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Ajustes de stock",
        reverse("ajuste_stock_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Referenciales",
        "#",
        icon="far fa-circle",
        children=referencial
    )
)

Menu.add_item("inventario", MenuItem("Inventario","#",icon='fa fa-warehouse',weight=6, children=children))