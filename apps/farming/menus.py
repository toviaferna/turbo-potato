from menu import Menu, MenuItem
from django.shortcuts import reverse


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
)

Menu.add_item("agricultura", MenuItem("Agricultura","#",icon='fa fa-tractor',weight=6, children=children))