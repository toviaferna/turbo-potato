from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    MenuItem(
        "Fincas",
        reverse("finca_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Calificaciones Agrícolas",
        reverse("calificacion_agricola_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Tipos de Actividades Agrícolas",
        reverse("tipo_actividad_agricola_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Tipos de Maquinarias Agrícolas",
        reverse("tipo_maquinaria_agricola_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Maquinarias Agrícolas",
        reverse("maquinaria_agricola_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Zafras",
        reverse("zafra_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Lotes",
        reverse("lote_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Plan de actividades por zafra",
        reverse("plan_actividad_zafra_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Contratos",
        reverse("contrato_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Acopios",
        reverse("acopio_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Actividades Agricolas",
        reverse("actividad_agricola_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Liquidaciones Agricolas",
        reverse("liquidacion_agricola_list"),
        icon="far fa-circle",        
    ),
    MenuItem(
        "Cierres de zafras",
        reverse("cierre_zafra_list"),
        icon="far fa-circle",        
    ),
)

Menu.add_item("agricultura", MenuItem("Agricultura","#",icon='fa fa-tractor',weight=6, children=children))
