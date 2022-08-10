from django.shortcuts import reverse
from menu import Menu, MenuItem

children = (
    
)

Menu.add_item("reportes", MenuItem("Reportes","#",icon='fa fa-file-contract',weight=8, children=children))
