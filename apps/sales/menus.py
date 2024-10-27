from django.shortcuts import reverse
from menu import Menu, MenuItem

referencial = (
    MenuItem(
        "Establecimientos",
        reverse("establecimiento_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Puntos de Expedicion",
        reverse("punto_expedicion_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Tipos de Documento",
        reverse("tipo_documento_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Tipos de Documento",
        reverse("tipo_documento_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Timbrados",
        reverse("timbrado_list"),
        icon="far fa-circle",
    ),
)

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
    MenuItem(
        "Notas de débito emitidas",
        reverse("nota_debito_emitida_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Notas de crédito emitidas",
        reverse("nota_credito_emitida_list"),
        icon="far fa-circle",
    ),
    MenuItem(
        "Cobros",
        reverse("cobro_list"),
        icon="far fa-circle",
    ),
        MenuItem(
        "Referenciales",
        "#",
        icon="far fa-circle",
        children=referencial
    ),
)

Menu.add_item("ventas", MenuItem("Ventas","#",icon='fa fa-cart-shopping',weight=7, children=children))
