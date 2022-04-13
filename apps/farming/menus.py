from menu import Menu, MenuItem
from django.shortcuts import reverse


children = (
    MenuItem(
        "Fincas",
        reverse("finca_list"),
        #icon="fa fa-map",        
    ),
)

Menu.add_item("agricultura", MenuItem("Agricultura","#",icon='fa fa-tractor',weight=6, children=children))